/*=================================*\
                                   
      Md. Shahidul Islam           
         CSE, BRUR                 
      Rangpur, Bangladesh          
 mail: shahidul.cse.brur@gmail.com 
 FB  : fb.com/shahidul.brur        
 Blog: shahidul-brur.blogspot.com 
\*=================================*/
#include<bits/stdc++.h>
using namespace std;
char s[1009];
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    //ios_base::sync_with_stdio(false); cin.tie(NULL);
    int t, k, n, i;
    
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        cin>>s>>k;
        n = strlen(s);
        int cnt = 0;
        bool pos = 1;
        for(int i = 0;i<n;i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                if(i+k>n)
                {
                    pos=0;
                    break;
                }
                for(int j = i, l = 1;l<=k;l++, j++)
                {
                    if(s[j]=='+')
                        s[j]='-';
                    else s[j] = '+';
                }
            }
        }
        cout << "Case #" << cas << ": ";
        if(pos)
            cout << cnt << "\n";
        else cout << "IMPOSSIBLE\n";
    }
    return 0;
}

