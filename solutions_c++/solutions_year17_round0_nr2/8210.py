#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

#define MOD 1000000007
#define ll long long


vector <int> dig(string s)
{
    vector <int> digits(s.length());

    for (int i = 0; i < s.length(); i++)
    {
        digits[i] = s[i] - '0';
    }
    return digits;
}

bool tidy(vector <int> num)
{
    for (int i = 0; i < num.size() - 1; i++)
    {
        if (num[i] > num[i + 1])
        {
            return false;
        }
    }
    return true;
}

string viToStr(vector <int> vec)
{
    string s = "";
    bool start = false;
    for (int i: vec)
    {
        if (i != 0)
        {
            start = true;
        }
        if (start)
        {
            char c = char(i + '0');
            s += c;
        }
    }
    return s;
}



int main()
{
    freopen("outputGCJforB.txt", "w", stdout);
    int t;

    cin>>t;



    for(int Tloop = 1; Tloop <= t; Tloop++)
    {
        string s;
        cin>>s;

        vector <int> fillNine(s.length() - 1, 9);
        fillNine.insert(fillNine.begin(), 0);

        cout<<"Case #"<<Tloop<<": ";
        if (s.length() == 1)
        {
            cout<<s<<endl;
        }
        else
        {
            vector <int> numDig = dig(s);
            while(!tidy(numDig) and numDig > fillNine)
            {

                for (int i =  0; i < s.length() - 1; i++)
                {
                    if(numDig[i] > numDig[i + 1])
                    {
                        numDig[i]--;
                        for (int j = 1; i + j < s.length(); j++)
                        {
                            numDig[i + j] = 9;
                        }

                    }

                }
                //cout<<"hi: "<<viToStr(numDig)<<endl;
            }

            cout<<viToStr(max(fillNine, numDig))<<endl;
        }

    }


    return 0;
}
