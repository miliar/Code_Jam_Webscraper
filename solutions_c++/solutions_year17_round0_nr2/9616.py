#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int qq,n,i,cnt=0,p,max;
    cin>>qq;
    while(qq--)
        { 
        cnt++;
        printf("Case #%d: ",cnt);
        scanf("%d",&n);
        
        for(i=1;i<=n;i++)
            {int flag=0;
            vector <int> d;
            if(i%10!=0)
                {
                p=i;
                
                while(p>0)
                    {
                    d.push_back(p%10);
                   
                
                    p=p/10;
                }
                for(int j=0;j<d.size()-1;j++)
                {if(d[j]>=d[j+1]);
                    else
                    {
                    flag=1;
                    break;
                    }
                }
           if(flag==0)
               max=i;
                
            }
             
        }
        cout<<max<<endl;
        
        
    }
    return 0;
}

