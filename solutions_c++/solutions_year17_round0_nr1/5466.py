#include <iostream>
#include <cstdio>
using namespace std;

int findIndex(char input[1000], int length, char symbol){
    int i = 0;
    while (input[i] != symbol && i < length)
        i++;

    return i;
}

long long findSmallest(char input[1000], int k, int length){
    int firstIndex = findIndex(input, length, '-');

    long long counter = 0;

    while (firstIndex <= length - k){
        counter++;

        for(int f = 0; f < k; f++)
            input[firstIndex + f] = (input[firstIndex + f] == '-' ? '+' : '-');

        firstIndex = findIndex(input, length, '-');
    }

    if (firstIndex > length - k && firstIndex < length)
        return -1;
    else
        return counter;
}

int main(){
    int cases;

    cin >> cases;

    char input[1001];

    for (int i = 0; i < cases; i++){
        cin >> input[0];
        int j = 0;
        while (input[j] != ' ')
        {
            j++;
            input[j] = cin.get();
        }
        int k;
        cin >> k;

        long long answer = findSmallest(input, k, j);
        if (answer == -1)
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i+1 << ": " << answer << endl;
    }

    return 0;
}
