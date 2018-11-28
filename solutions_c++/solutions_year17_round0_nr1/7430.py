#include<iostream>
using namespace std;

int count = 0;
int flag1 = 0;
void check(string &str, int k, string temp)
{
    flag1 = 0;
    count = 0;
    int i = 0;
    while( i < str.size() )
    {
        if((i + k <= str.size()) && str[i] == '-')
        {
            count++;
            int l;
            for(l = 0; l < k; l++)
            {
                if(str[i+l] == '+')
                    str[i+l] = '-';
                else
                    str[i+l] = '+';
            }
        }
        if(str.compare(temp) == 0)
        {
            break;
            flag1 = 1;
        }
        i++;
    }
}

int main()
{
    int tests;
    int counter =1;
    cin >> tests;
    while(tests > 0)
    {
        string str;
        int k;
        cin >> str >> k;
        string temp = str;
        string save = str;
        for(int i = 0; i < str.size(); i++)
            temp[i] = '+';
        check(str,k,temp);
        if(str.compare(temp) == 0)
            flag1 = 1;
        if(flag1 == 1)
        {
            cout << "Case #" << counter << ": " << count << endl;
        }
        else
        {
            cout << "Case #" << counter << ": " << "IMPOSSIBLE" << endl;
        }
        counter++;
        tests--;
    }
}
