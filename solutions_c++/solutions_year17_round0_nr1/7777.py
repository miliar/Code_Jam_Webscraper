#include <iostream>
#include <string>
#include <fstream>

using namespace std;
void turn(string &s, int j, int k){
    for(int i=0;i<k;i++)
    {
        if(s[j+i]=='+') s[j+i]='-';
        else s[j+i]='+';
    }
}

int main()
{
    ifstream in("pancakein.txt");
    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    ofstream out("pancakeout.txt");
    streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!


    int n;
    cin>>n;
    for(int i=0;i<n;++i)
    {
        string s;
        int k;
        cin>>s>>k;

        int j=0;
        int c=0;
        while(j<=s.size()-k)
        {
            if(s[j]=='-')
            {
                turn(s,j,k);
                c++;
            }
            j++;
        }
        bool l=true;
        while(l and j<s.size())
        {
            l=(s[j]=='+');
            j++;
        }
        if(l)
        {
            cout<<"Case #"<<i+1<<": "<<c<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        }
    }

    return 0;
}
