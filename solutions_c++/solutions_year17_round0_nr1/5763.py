#include <bits/stdc++.h>

using namespace std;

int encode(string s)
{
    int q=0;
    int a=0;
    for(int i=s.size()-1;i>=0;i--)
    {
        if(s[i]=='+')
        q+=1<<a;
        a++;
    }
    return q;
        
}
bool ok(string s)
{
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='-')
        return false;
    }
    return true;
}
int main()
{
    int t,a;
    
    cin >> t;
    for(int caso=1;caso<=t;caso++)
    {   
        queue<pair<string,int> > cola;
        string s ;
        int p;
        cin >> s >> a;
        
        cola.push(pair<string,int>(s,0));
        map<int,int> e;
        int sss = -1;
        while(!cola.empty())
        {
           
            string r = cola.front().first;
            int step=cola.front().second;
            cola.pop();
             int code = encode(r);
            if(ok(r))
            {
                sss=step;
                break;
            }
                
          
            
            if(e.find(encode(r))==e.end())
            {
                e[encode(r)]=1;
                for(int i=0;i<=r.size()-a;i++)
                {
                    string c = r;
                    for(int k=0;k<a;k++)
                    {
                        c[i+k]= c[i+k]=='+'?'-':'+';
                    }
                    if(e.find(encode(c))==e.end())
                    {
                        cola.push(pair<string,int>(c,step+1));
                    }
                    
                }
            }
            
        }
        printf("Case #%d: ",caso);
        sss==-1?printf("IMPOSSIBLE\n"):printf("%d\n",sss);
    }
    
    return 0;
}