import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
import algorithms


Algorithm = None
title = None
description = None
bigO = None

#Draw and update plot
def draw_Sort():
    # Initialize fig
    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rec = ax.bar(range(len(array)), array, align='edge', color = "GREEN", edgecolor="BLACK")

    ax.set_xlim(0, len(array))
    ax.set_ylim(0, int(len(array) * 1.1))
    text = ax.text(0, 1.02, "", transform=ax.transAxes)

    epochs = [0]
    def update_plot(array, rec, epochs):
        for rec, val in zip(rec, array):
            rec.set_height(val)
        epochs[0] += 1
        text.set_text("Operations: {}".format(epochs[0]))

    anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=Algorithm, interval=1, repeat=False)
    plt.show()

# Define the window's contents
layout = [[sg.Text("Number of Elements")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('Bubble Sort'), sg.Button('Insertion Sort'), sg.Button('Quick Sort'), sg.Button('Count Sort')],
          [sg.Button('Selection Sort'), sg.Button('Merge Sort'), sg.Button('Heap Sort'), sg.Button('Shell Sort')],
          [sg.Text(size=(100, 1), key='-OUTPUT-')],
          [sg.Text("Current Algorithm: "), sg.Text(size=(100, 1), key='-ALGO-')],
          [sg.Text("Big O: "), sg.Text(size=(100, 1), key='-BIGO-')],
          [sg.Text("Description: "), sg.Text(size=(100, 1), key='-DESCRIPTION-')],
          [sg.Button('Run'), sg.Button('Quit')]]
window = sg.Window('Algorithm Visualizer', layout)


#Event handler
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        quit()

    # See if run was executed and inputs are valid
    if event == 'Run' and  values['-INPUT-'] != '' and Algorithm != None and algSelected == True:
        draw_Sort()


    # must be algorithm selected, ensure elements input and update algorithm selected
    if values['-INPUT-'] == '':
        window['-OUTPUT-'].update("Enter a value for the number of elements, and select an algorithm")
    else:
        window['-OUTPUT-'].update("")
        array = [i + 1 for i in range(int(values['-INPUT-']))]
        random.shuffle(array)

        algSelected = True
        #Check which algorithm was selected, change update values
        if event == 'Bubble Sort':
            Algorithm = algorithms.sort_bubble(array)
            title = "Bubble Sort"
            bigO = "O(N^2)"
            description = "Checks neighboring data and swaps if they are in incorrect order"
        elif event == "Insertion Sort":
            Algorithm = algorithms.insertion_sort(array)
            title = "Insertion Sort"
            bigO = "O(N^2)"
            description = "Iterates through transferring elements into a sorted portion of the array one at a time"
        elif event == "Quick Sort":
            Algorithm = algorithms.quick_Sort(array, 0, len(array)-1)
            title = "Quick Sort"
            bigO = "O(N^2)"
            description = "Partions data around a pivot point, one for higher values and one for lower. Calls itself recursively to sort"
        elif event == "Selection Sort":
            Algorithm = algorithms.selection_sort(array)
            title = "Selection Sort"
            bigO = "O(N^2)"
            description = "Finds and places the smallest element at each location"
        elif event == "Merge Sort":
            Algorithm = algorithms.merge_sort(array, 0, len(array)-1)
            title = "Merge Sort"
            bigO = "O(N Log(N))"
            description = "Divides array into sublists, sorts and merges the sorted sublists"
        elif event == "Heap Sort":
            Algorithm = algorithms.heap_sort(array)
            title = "Heap Sort"
            bigO = "O(N Log(N))"
            description = "Builds a heap of the data (complete binary tree structure) and moves the largest element (root) of the heap into the array until sorted"
        elif event == "Shell Sort":
            Algorithm = algorithms.shell_sort(array)
            title = "Shell Sort"
            bigO = "O(N^2)"
            description = "Sort sublists along a distance from each other, progressive reduce the gap until the array is sorted"
        elif event == "Count Sort":
            Algorithm = algorithms.count_sort(array)
            title = "Count Sort"
            bigO = "O(N + K)"
            description = "Counts how many times each item appears, goes through array again and fills in all locations accordingly"
        else:
            algSelected = False

    #Update information for algorithms
    window['-BIGO-'].update(bigO)
    window['-DESCRIPTION-'].update(description)
    window['-ALGO-'].update(title)
# Finish up by removing from the screen
window.close()