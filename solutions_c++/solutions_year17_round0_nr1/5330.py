#include <iostream>
#include <cstring>

using namespace std;

int main() {
    char S[1002];
    int T,l,i,k,j,t,cnt;
    freopen("s.txt", "r", stdin);
    freopen("ss.txt", "w", stdout);
    scanf("%d", &T);
   for (t=0 ;t < T;t++) {
       cnt=0;
        scanf("%s %d", S,&k);

        l = strlen(S);
        for(i =0 ; i< l/2 ;i++)
        {
             if(S[i] == '-')
             {
                 cnt++;
                 for (j = 0; j < k; j++)
                     S[i + j] = (S[i + j] == '-' ? '+' : '-');
             }
            if(S[l-i-1] == '-')
            {   cnt++;
                for(j=0 ; j < k ; j++)
                    S[l-i-1-j]=(S[l-i-1-j] == '-'?'+':'-');
            }
        }
        bool pos=true;
       for(i =0 ; i< k ;i++)
       {
           if( l/2-i > -1 && S[l/2+i] == '-' )
           {   pos=false;break;
           }
           if (l/2-i < l && S[l/2-i] == '-')
           {
               pos=false;break;
           }
       }
       //cout << S << endl;
       if(pos) printf("Case #%d: %d", t+1,cnt);
       else printf("Case #%d: IMPOSSIBLE", t+1);

       if(t != T-1)
           printf("\n");
    }
}


