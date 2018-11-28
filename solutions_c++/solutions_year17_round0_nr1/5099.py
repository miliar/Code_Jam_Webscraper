#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <list>
#include <fstream>

using namespace std;

int main() {
    ifstream myReadFile;
    myReadFile.open("C:\\Users\\007\\CLionProjects\\untitled\\text.txt");
    ofstream myReadFile1;
    myReadFile1.open("C:\\Users\\007\\CLionProjects\\untitled\\text1.txt");
    int t;
    myReadFile >> t;
    for(int i = 0; i < t; ++i)
    {
        string arr;
        int k;
        bool ok = true;
        int counter = 0;
        myReadFile >> arr;
        myReadFile >> k;
        for(int i = 0; i < arr.size(); ++i)
        {

            while( i < arr.size() && arr[i] == '+') ++i;
            if(i < arr.size() && i + k > arr.size())
            {
                ok = false;
                break;
            }
            if(i == arr.size()) break;
            for(int j = i; j < i + k; ++j)
            {
                arr[j] = arr[j] == '+' ? '-' : '+';
            }
            counter++;
        }
        myReadFile1 << "Case #" << i + 1 << ": ";
        ok ? myReadFile1 << counter << endl : myReadFile1 << "IMPOSSIBLE" << endl;
    }
    return 0;
}

