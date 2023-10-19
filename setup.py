from setuptools import setup, find_packages

setup(
    name='runreveal',
    version='0.0.4',
    author='Evan Johnson',
    author_email='evan@runreveal.com',
    description='Interact with the RunReveal API',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

