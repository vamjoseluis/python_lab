

### Pyenv
You can use Pyenv to work with different versions of Python. Follow the below steps to install it.

- Install pyenv

```
$ brew install pyenv
```

- Add pyenv initializer to shell
```
$ echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
```

- Reload the bash_profile
```
source ~/.bash_profile
```

- View the python versions installed
```
pyenv versions
```

Set global python
```
$ pyenv global <version>
```

