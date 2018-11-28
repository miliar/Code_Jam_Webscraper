//
// Created by 007 on 09.04.2017.
//

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
    for(int i = 0; i < t; ++i) {
        string arr;
        int k;
        bool ok = true;
        myReadFile >> arr;
        for(int j = arr.size() - 1; j > -1; --j)
        {
            while(j > 0 && int(arr[j]) >= int(arr[j - 1])) --j;
            if(j == 0) break;
            for(int k = j; k < arr.size(); ++k)
                arr[k] = '0' + 9;
            arr[j - 1]--;
        }
        if(arr[0] == '0' && arr.size() > 1) arr.erase(arr.begin());
        myReadFile1 << "Case #" << i + 1 << ": " << arr << endl;
    }
    return 0;
}