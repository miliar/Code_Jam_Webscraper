#include <iostream>
#include <string>

using namespace std;


string changeindex(string s,int x)
{


    char num[] = {'0','1','2','3','4','5','6','7','8','9'};

    for(int j=0;j<10;j++)
        if(num[j]==s[x])
        {
            s[x] = num[j-1];
        }

    return s;
}

string lasttidy(unsigned long long int n)
{

    std::string s;
    s = std::to_string(n);

    if(s.size()==1) return s;

    for(int i=1;i<s.size();i++)
    {
        if(s[i]<s[i-1])
        {

           s = changeindex(s,i-1);

            for(int j=i;j<s.size();j++)
                s[j] = '9';

             return lasttidy(stoull(s));

        }

    }

    return s;

}

int main(int argc, char *argv[])
{

    int tc; cin >> tc;
    for(int i=1;i<=tc;i++)
    {
        unsigned long long int number;
        cin >> number;
        cout << "Case #"<<i<<": "<< lasttidy(number)<<"\n";
    }

    return 0;
}

