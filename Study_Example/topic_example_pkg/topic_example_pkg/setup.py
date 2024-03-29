from setuptools import setup

package_name = 'topic_example_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ydh',
    maintainer_email='ydh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_publisher=topic_example_pkg.topic_publisher:main',
            'topic_subscriber=topic_example_pkg.topic_subscriber:main',
        ],
    },
)
