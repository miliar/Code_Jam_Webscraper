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
        int k;
        cin>>s>>k;
        int counter = 0;
        bool failed = false;
        for (int i = 0; i<s.length(); i++)
        {
            if(s[i] == '-')
            {
                if(i + k > s.length())
                {
                    failed = true;
                }
                else
                {
                counter++;
                    for(int j = 0;j<k;j++)
                    {
                        if(s[i+j] == '+')
                        {
                            s[i+j] = '-';
                        }
                        else
                        {
                            s[i+j] = '+';
                        }
                    }
                }
            }
        }

        cout<<"Case #"<<caseCounter<<": ";
        if(failed)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<counter<<endl;
        }
    }
    cout.close();
    return 0;
}
