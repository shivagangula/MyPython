**What is identifier ?**

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore ( _ ) followed by zero or more letters, underscores and digits ( 0 to 9 ).

- Python does not allow punctuation characters such as @, $, and % within identifiers.
```python
my_variable = 10 # valid
my@variable = 10 # not vaild because @ is there in 
```
- Python is a case sensitive programming language. Thus, my_variable and My_variable are two different identifiers in Python.

```python
my_variable = 10 
My_variable = 10 
#both are have different
```
**Here are naming conventions for Python identifiers**

- Class names start with an uppercase letter. All other identifiers start with a lowercase letter.

- Starting an identifier with a single leading underscore indicates that the identifier is private.

- Starting an identifier with two leading underscores indicates a strongly private identifier.

- If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

