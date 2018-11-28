#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    ofstream cout;
    cout.open ("example.txt");
    ifstream cin;
    cin.open("input.txt");
    int test;
    cin >> test;
    int caseCounter=0;
    while (test--)
    {
    caseCounter++;
        string s;
        cin>>s;
        bool isTiny = false;
        while(!isTiny)
        {
        isTiny = true;
        bool convertToMax = false;
        for (int i = 0; i<s.length(); i++)
        {
        if(convertToMax)
        {
            s[i] = '9';
            continue;
        }
            if(i + 1 < s.length() && s[i] > s[i + 1])
            {
            isTiny = false;

                    int k = i;
                if(s[i] == '0')
                {
                    while(k == '0')
                    {
                        s[k] = '9';
                        k--;
                    }

                }
                 s[k]--;
                convertToMax = true;
                s[i + 1] = '9';

            }
        }
        }
        cout<<"Case #"<<caseCounter<<": ";
        bool notZero = false;
        if(s.length() == 1 && s[0] == '0')
        {
            notZero = true;
        }
        for(int i=0;i<s.length();i++)
        {
            if(notZero || s[i] != '0')
            {
                notZero = true;
                cout<<s[i];
            }
        }
            cout<<endl;

    }
    cout.close();
    return 0;
}
