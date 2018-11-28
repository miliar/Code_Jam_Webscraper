#include <iostream>

using namespace std;

char swapper(char S)
{
    if(S == '-') return '+';
    else return '-';
}

int flipperCounter(string S, int K)
{
    int valueToReturn = 0;
    int counter = 0;
    while (counter + K <= S.length())
    {
        if(S[counter] == '-')
        {
            for(int j = counter; j < counter+K; j++)
                S[j] = swapper(S[j]);
            valueToReturn++;
        }
        counter++;
    }

    for(int i = S.length()-1; i >= 0; i--)
        if(S[i] == '-') return -1;

    return valueToReturn;
}

int main()
{
    int T,K;
    string S;

    cin >> T;

    int value;
    for(int i = 0; i < T; i++)
    {
        cin >> S >> K;

        value = flipperCounter(S,K);

        if(value == -1) cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
            else cout << "Case #" << i+1 << ": " << value << endl;
    }
    return 0;
}
