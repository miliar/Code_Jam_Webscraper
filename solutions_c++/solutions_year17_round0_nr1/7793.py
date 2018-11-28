#include<bits/stdc++.h>
using namespace std;
int main()
{ freopen("A-large.in", "r", stdin);
  freopen("outLA.txt", "w", stdout);
  int T, k, c=0;
  string s;
  cin>>T;
  for(int I=1;I<=T;++I)
  { cin>>s>>k;
    c=0;
    int i;
    for(i=0;i<=s.length()-k;++i)
    { if(s[i]=='-')
      { for(int j=1;j<k;++j)
        { if(s[i+j]=='-')s[i+j]='+';
          else s[i+j]='-';
        }
        ++c;
      }
    }
    for(;i<s.length();++i)
    { if(s[i]=='-')
      { break;
      }
    }
    if(i==s.length())
    { cout<<"Case #"<<I<<": "<<c<<"\n";
    }
    else
    { cout<<"Case #"<<I<<": IMPOSSIBLE"<<"\n";
    }
  }
}
