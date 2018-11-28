#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, m;
  string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int g = 1; g <= t; ++g) {
    cin >> s >> m;  // read n and then m.
   int count=0;
   int test=0;
    for(int i=0;i<s.length();i++)
    {  // cout<<s[i]<<endl;
        if(s[i]=='-')
        {//cout<<i;
                if(i+m <s.length()){
                    for(int j=i;j<i+m;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else s[j]='-';
                    }
                    count++;
                   // cout<<s<<"asdasd"<<i;
                }
                else if(i+m ==s.length())
                {
                    for(int j=i;j<i+m;j++)
                    {
                        if(s[j]=='+')
                            {
                            test=1;
                            break;}
                         else s[j]='+';
                     //   cout<<s<<"assdsdaddasd"<<i;
                    }
                    // cout<<s<<"asdssasd"<<i;
                    count++;
                }
                else if(i+m >s.length())
                {

                     test=1;
                  //    cout<<s<<"aerfgsdasd"<<i;
                     break;

                }
        }
    }
    if(test==1)
        cout<<"Case #"<<g<<": IMPOSSIBLE"<<endl;
    else
        cout << "Case #" <<g<< ": " <<count<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
