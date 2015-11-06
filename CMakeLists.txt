CMAKE_MINIMUM_REQUIRED( VERSION 2.6 )
CMAKE_POLICY(VERSION 2.6)
project(MergeLabels)

find_package(SlicerExecutionModel REQUIRED)
include( ${SlicerExecutionModel_USE_FILE} )
find_package(ITK REQUIRED)
include(${ITK_USE_FILE})


set(Filter ThresholdFilter)

SEMMacroBuildCLI(
    NAME MergeLabels
    EXECUTABLE_ONLY
    TARGET_LIBRARIES ${ITK_LIBRARIES}
)
