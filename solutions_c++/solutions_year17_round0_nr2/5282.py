#include<bits/stdc++.h>
using namespace std;
string getAnswer(string s)
{
    if(s.length()==1)
        return s;
    else
    {
        for (int i=0;i<s.length()-1;i++)
        {
            string firstLetter(1,s[i]);
            string secondletter(1,s[i+1]);
            if(stoll(firstLetter,NULL,0) > stoll(secondletter,NULL,0))
            {
                 if(stoll(s.substr(i,2),NULL,0)==10 && i==0)
                 {
                     s=s.substr(0,i)+"9"+s.substr(i+2);
                    // cout<<s<<endl;
                     for(int j=i+1;j<s.length();j++)
                     {
                         s=s.substr(0,j)+"9"+s.substr(j+1);
                     }
                 }
                 else
                 {
                      string temp=to_string(stoll(s.substr(i,2))-1);
                      if(temp.length()==1)
                        temp="0"+temp;
                        s=s.substr(0,i)+temp+s.substr(i+2);
                        for(int j=i+2;j<s.length();j++)
                        {
                            s=s.substr(0,j)+"9"+s.substr(j+1);
                        }

                 }
                return getAnswer(s);
            }


        }
          return s;
    }
}
int main()
{
    long long t,n;
    int test_case=1;
    ifstream in_file;
    in_file.open("input4.in");
    ofstream out_file;
    out_file.open("out.in");
    in_file>>t;
    while(t--)
    {
      in_file>>n;
      string s = to_string(n);
      out_file<<"Case #"<<test_case<<": "<<getAnswer(s)<<"\n";
      test_case++;
    }
    return 0;
}
