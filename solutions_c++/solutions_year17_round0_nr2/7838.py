#include <bits/stdc++.h>

using namespace std;

int main()
{
 freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
    int T,i,j,b=1;
    string s;
    scanf("%d",&T);
    while(T--)
    {
        cin>>s;
        int le=s.length();
        for(i=le-2;i>=0;i--)
        {
            if(s[i]>s[i+1]){
                s[i]--;
                for(j=i+1;j<le;j++){s[j]='9';}
            }
        }

        if(s[0]=='0')s.erase(0,1);
        cout<<"Case #"<<b++<<": "<<s<<endl;

    }





    return 0;
}
