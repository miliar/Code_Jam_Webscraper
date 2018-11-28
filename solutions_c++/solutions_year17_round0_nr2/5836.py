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

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B_large.out", "w", stdout);
    //ios_base::sync_with_stdio(false); cin.tie(NULL);
    char s[100];
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        cin>>s;
        int n = strlen(s);
        bool f=0;
        int p = -1;
        for(int i = 0;i<n-1;i++)
        {
            if(s[i]>s[i+1])
            {
                f=1;
                s[i]--;
                p = i;
                for(int j = i+1;j<n;j++)
                    s[j] = '9';
                break;
            }
        }
        while(f==1)
        {
            f = 0;
            for(int i = 0;i<p;i++)
            {
                if(s[i]>s[i+1])
                {
                    f=1;
                    s[i]--;
                    for(int j = i+1;j<=p;j++)
                        s[j] = '9';
                    p = i;
                    break;
                }
            }
        }
        cout << "Case #" << cas << ": ";
        if(s[0]>'0')
            cout << s[0];
        for(int i =1;i<n;i++)
            cout << s[i];
         cout << "\n";
    }
    return 0;
}


