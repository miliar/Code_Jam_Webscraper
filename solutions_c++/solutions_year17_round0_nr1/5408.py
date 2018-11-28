#include <iostream>
#include <string.h>
using namespace std;

void flip_subset(char S[2000], int start, int end)
{
    for(int i = start; i <= end && start >= 0; i++)
    {
        if(S[i] == '-')
            S[i] = '+';
        else
            S[i] = '-';
    }
    return;
}

bool check(char S[2000])
{
    for(int i = 0; S[i] != '\0'; i++)
        if(S[i] == '-')
            return false;
    return true;
}

int main()
{
    int T, N;
    char S[2000];
    cin >> T;

    for(int x = 0; x < T; x++)
    {
        cin >> S >> N;
        int len = strlen(S);
        int i = 0, j = len - N;
        int count = 0, flips = 0;
        while(j >= 0)
        {
            i = j + N - 1;
            count = 1;
            while(count <= N && i >= 0){
                if(S[i] == '-')
                {
                    flip_subset(S, i - N + 1, i);
                    flips++;
                    break;
                }
                i--;
                count++;
            }
            j--;
        }
        if(check(S))
            cout << "Case #" << x+1 << ": " << flips << endl;
        else
            cout << "Case #" << x+1 << ": IMPOSSIBLE" << endl;
    }
}
