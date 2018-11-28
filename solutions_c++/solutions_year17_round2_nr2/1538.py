#include <bits/stdc++.h>

using namespace std;

char letra(int i)
{
    i++;
    switch(i)
    {
        
        case 1: return 'R';
        case 2: return 'O';
        case 3: return 'Y';
        case 4: return 'G';
        case 5: return 'B';
        case 6: return 'V';
    }
    
}
int main()
{
    int casos;
    cin >> casos;
    
    for(int caso=1;caso<=casos;caso++)
    {
        vector<int> p;
        int n;
        cin >> n;
        for(int i=0;i<6;i++)
        {
            int a;
            cin >> a;
            p.push_back(a);
        }
        vector<int> ans ;
        int pos =20;
        int lastpos=20;
        for(int i=0;i<n ;i++)
        {
            int maximo=0;
            for(int k=0;k<6;k++)
            {
              //  printf("%d %d\n",k,lastpos);
                if((lastpos > 10 ||abs(k-lastpos)%6>1) && p[k]>maximo)
                {
                   
                    maximo=p[k];
                  //   printf("%d maximo\n",maximo);
                   
                    pos=k;
                     if(lastpos==20)
                    break;
                }
            }
         //   printf("salio\n");
         
            if(maximo==0)
            {
                pos=-20;
            }
            else
            {
                ans.push_back(pos);
                lastpos=pos;
                p[pos]-=1;
            }
            
            
        }
         if(ans.size()!=0 && abs(ans[ans.size()-1]-ans[0])<=1)
                pos=-20;
           
        printf("Case #%d: ",caso);
        if(pos==-20)
        {
            printf("IMPOSSIBLE");
        }
        else
        {
            for(int i=0;i<ans.size();i++)
            {
                printf("%c",letra(ans[i]));
            }
        }
        printf("\n");
    }
    return 0;
}