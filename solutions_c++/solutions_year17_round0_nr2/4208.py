#include <bits/stdc++.h>

using namespace std ;

int isValid(string data)
{
    int tidy = -1 ;

    int length = data.size() ;
    for(int i = 0 ; i < length -1 ;i++)
    {
        if(data[i] > data[i+1])
        {
            return i;
        }
    }
    return tidy;
}

int main()
{
    freopen("B-large.in", "r" , stdin);
    freopen("B_output.txt", "w" , stdout);
    int T ;
    string input;
    long long int output ;
    scanf("%d", &T);

    for(int i = 0 ; i < T ; i++)
    {
        cin >> input;
        int return_value= isValid(input);
        int length = input.length();
        while(return_value != -1)
        {
            input[return_value]--;
            for(int j = return_value+1 ; j < length ; j++)
            {
                input[j] = '9';
            }
            return_value= isValid(input);
        }
        stringstream convert(input);
        convert>>output;
        cout << "Case #" << i+1 <<": " << output << endl;
    }
    return 0;
}
