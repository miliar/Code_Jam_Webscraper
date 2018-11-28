#include <iostream>
#include <vector>
//#include <unordered_set>

using namespace std;

int main()
{
  int n;
  cin>>n;
  for (int i=1;i<=n;i++)
  {
    string s;
    //unordered_set<string> ss;
    cin>>s;
    //vector<string> q1,q2;
    int a,lv=0;
    cin>>a;
    cout<<"Case #"<<i<<": ";
    /*q1.push_back(s);
    while (true)
    {
      if (q1.size()==0)
      {
        cout<<"IMPOSSIBLE"<<endl;
        break;
      }
      bool x=0;//cout<<lv<<endl;
      for (int j=0;j<q1.size();j++)
      {//cout<<q1[j]<<endl;
        bool z=1;
        for (int k=0;k<q1[j].size();k++)
          if (q1[j][k]=='-')
            z=0;
        if (z)
        {
          cout<<lv<<endl;
          x=1;
          break;
        }
        for (int k=0;k<=q1[j].size()-a;k++)
        {
          s=q1[j];
          for (int l=0;l<a;l++)
            if (s[l+k]=='+')
              s[l+k]='-';
            else
              s[l+k]='+';
          if (ss.count(s)==0)
            q2.push_back(s);
          ss.insert(s);
        }
      }
      if (x)
        break;
      lv++;
      q1=q2;
      q2.clear();
    }*/
    
    int y=0;
    for (int j=0;j<=s.size()-a;j++)
      if (s[j]=='-')
      {
        y++;
        for (int k=0;k<a;k++)
          if (s[k+j]=='+')
            s[j+k]='-';
          else s[j+k]='+';
      }
    for (int j=s.size()-a+1;j<s.size();j++)
      if (s[j]=='-')
        y=-1;
    if (y!=-1)
    cout<<y<<endl;
    else
      cout<<"IMPOSSIBLE\n";
  }
  return 0;
}
