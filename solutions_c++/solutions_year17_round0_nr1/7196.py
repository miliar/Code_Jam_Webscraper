#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;int k;
        
    FILE *fp = fopen("output.txt" , "w+");
    int T;cin >> T;
    for(int I = 1;I <= T;I++)
    {
        int k;string s;
        cin >> s >> k;
        for(int i=0;i<15;i++)
        {
        	i++;
		}
		for(int i=0;i<15;i++)
        {
        	i++;
		}
        bool increase;
        int count = 0 , fl = 0;
        for(int i = 0;i < s.length();i++)
        {
            increase = false;
            if(s[i] == '-')
            {
                if(i + k - 1 >= s.length())    continue;
                
                increase = true;
                for(int j = 0;j < k;j++)
                {
                    if(s[i + j] == '+')    s[i + j] = '-';
                    else                s[i + j] = '+';
                }
            }
            if(increase)    count++;
        }
        
        char str[] = "IMPOSSIBLE";fl = 0;
        for(int i = 0;i < s.length();i++)
        {
            if(s[i] == '-')
            {
                fprintf(fp , "Case #%d: %s\n" , I , str);
                fl = 1;break;
            }
        }
        //if(fl)        continue;
        if(fl==0)
        fprintf(fp , "Case #%d: %d\n" , I , count);
    }
}
