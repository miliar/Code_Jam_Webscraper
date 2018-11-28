#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    int T,t;
    cin>>T;
    for (t=0; t<T; t++) {
        int N, R, O, Y, G, B, V;
        cin>>N>> R>> O>> Y>> G>> B >> V;
        string s;
        bool imp = false;
        if (R> 0) {
            s = "R";
            R--;
        }
        else if(Y> 0){
            s = "Y";
            Y--;
        }
        else{
            s = "B";
            B--;
        }
        N-=1;
        int cl = 1;
        while (N > 0)
        {
            cl = s.size();
            char c = s[cl-1];
            switch (c) {
                case 'R':{
                    if(B == 0 && Y==0)
                    {
                        imp = true;
                    }
                    else if(B>Y)
                    {
                        s += "B";
                        B--;
                    }
                    else
                    {
                        s+="Y";
                        Y--;
                    }
                    break;
                }
                case 'Y':{
                    if(B == 0 && R==0)
                    {
                        imp = true;
                    }
                    else if(R>=B)
                    {
                        s += "R";
                        R--;
                    }
                    else
                    {
                        s+="B";
                        B--;
                    }
                    break;
                    
                }
                case 'B':
                {
                    if(Y == 0 && R==0)
                    {
                        imp = true;
                    }
                    else if(R>=Y)
                    {
                        s += "R";
                        R--;
                    }
                    else
                    {
                        s+="Y";
                        Y--;
                    }
                    break;
                }
                default:
                    break;
            }
            N--;
            if(imp)
                break;
        }
        if (s[0] == s[s.size()-1]) {
            imp = true;
        }
        if (imp) {
            s="IMPOSSIBLE";
        }
        cout <<"Case #"<<t+1<<": "<< s <<endl;
    }
    
    return 0;
}