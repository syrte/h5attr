# H5Attr
H5Attr: Quick access to hdf5 data via attributes, allowing `group.key` instead of `group['key']` and IPython/Jupyter tab completion.

## Installation

```bash
pip install h5attr
```
[not available yet]

## Usage
```
# create example HDF5 file
import h5py, io
file = io.BytesIO()
with h5py.File(file, 'w') as fp:
    fp['0'] = [1, 2]
    fp['a'] = [3, 4]
    fp['b/c'] = 5
    fp.attrs['d'] = 's'

# open file
f = H5Attr(file)

# easy access to members, with tab completion in IPython/Jupyter
f.a, f['a']

# also work for subgroups, but note that f['b/c'] is more efficient
# because it does not create f['b']
f.b.c, f['b'].c, f['b/c']

# convert integer keys to strings automatically (cannot use f.0)
f[0], f['0']

# allow dict-like operations
list(f), [key for key in f], 'a' in f

# access to HDF5 attrs via a H5Attr wrapper
f._attrs.d, f._attrs['d']

# show summary of the data
f._show()
# 0   int64 (2,)
# a   int64 (2,)
# b/  1 members

# close the hdf5 file
f._close()

# lazy (default) and non-lazy mode
f = H5Attr(file)
f.a  # <HDF5 dataset "a": shape (2,), type "<i8">

f = H5Attr(file, lazy=False)
f.a  # array([3, 4])
```


## API
`H5Attr(path, lazy=True, **args)`

- Parameters
    - `path`: h5py Group, file path, or file-like object.
    - `lazy`: bool, if true, dataset[()] will be returned.
    - `args`: additional arguments used for opening HDF5 file.

- Properties
    - `_attrs`: access to the h5py attrs dict.

- Methods
    - `_close()`: close the h5py file if applicable.
    - `_show()`: show a summary of the h5py group.
