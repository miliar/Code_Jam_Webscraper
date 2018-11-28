/*
 *    Google Code Jam R1B B
 */
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath> 
#include <algorithm>
#include <vector>
#include <list>
#include <cstring>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <queue>
#include <deque>
#include <ctime>
#include <complex>
#include <bitset>
#include <time.h>
#include <iomanip>
#include <cassert>

using namespace std;
#define PB push_back
#define LL long long
#define MP make_pair
#define fi first
#define se second
typedef unsigned long long ULL;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define DBG 0

#define fori(i,a,b) for(int i = (a); i < (b); i++)
#define forie(i,a,b) for(int i = (a); i <= (b); i++)
#define ford(i,a,b) for(int i = (a); i > (b); i--)
#define forde(i,a,b) for(int i = (a); i >= (b); i--)
#define forls(i,a,b,n) for(int i = (a); i != (b); i = n[i])
#define mset(a,v) memset(a, v, sizeof(a))
#define mcpy(a,b) memcpy(a, b, sizeof(a))

#define MIN_LD -2147483648
#define MAX_LD  2147483647
#define MIN_LLD -9223372036854775808
#define MAX_LLD  9223372036854775807
#define MAX_INF 18446744073709551615
const int INF = 0x7fffffff;
typedef set<int> Set;
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
//set_union(ALL(x1),ALL(x2),INS(x)),set_intersection

int T, N;
int R,O,Y,G,B,V;
string imp = "IMPOSSIBLE";

int main(void){
    
    //freopen("*.in", "r", stdin);
    //freopen("*.out", "w", stdout);
    cin.sync_with_stdio(false);
    cin >> T;
    forie(t,1,T){
        cout << "Case #" << t << ": ";
        cin >> N >> R >> O >> Y >> G >> B >> V;
        //
        if(O>0 && B+O==N){
            if(B!=O){cout << imp << endl; continue;}
            string ans = "";
            fori(i,0,B)ans+="BO";
            cout << ans << endl;
            continue;
        }
        if(G>0 && R+G==N){
            if(R!=G){cout << imp << endl; continue;}
            string ans = "";
            fori(i,0,R)ans+="RG";
            cout << ans << endl;
            continue;
        }
        if(V>0 && Y+V==N){
            if(Y!=V){cout << imp << endl; continue;}
            string ans = "";
            fori(i,0,Y)ans+="YV";
            cout << ans << endl;
            continue;
        }
        
        //
        if((O>0 && B<=O) || (G>0 && R<=G) || (V>0 &&Y<=V)){cout << imp << endl; continue;}

        string SO,SG,SV; SO=SG=SV="";
        if(O>0){
            //BOBOB
            SO = "B";
            fori(i,0,O)SO+="OB";
            B -= O+1;
            O = 1;
        }
        if(G>0){
            //RGRGR
            SG = "R";
            fori(i,0,G)SG+="GR";
            R -= G+1;
            G = 1;
        }
        if(V>0){
            //YVYVY
            SV = "Y";
            fori(i,0,V)SV+="VY";
            Y -= V+1;
            V = 1;
        }

        //
        N = B + O + R + G + Y + V;
        if(2*(B+O)>N || 2*(R+G)>N || 2*(Y+V)>N){cout << imp << endl; continue;}
        string ans = "";
        /*
        int submax = max(B+O,max(R+G,Y+V));
        int k = 0;
        if(B+O==submax){
            while(B+O>0){
                if(B>0){
                    ans+="B";
                    B--;
                }
                else{
                    ans+=SO;
                    O--;
                }
            }
            k = 0;
            while(R+G>0){
                if(k==0){
                    if(R>0){
                        ans = "R"+ans;
                        R--;
                        k++;
                    }
                    else{
                        ans = SG+ans;
                        G--;
                        k+=SG.size();
                    }
                }
                else{
                    while(ans[k]=='O'||ans[k-1]=='O'||ans[k]=='V'||ans[k-1]=='V'||ans[k]=='R'||ans[k-1]=='R')k++;
                    if(R>0){
                        ans.insert(k,"R");
                        R--;
                        k++;
                    }
                    else{
                        ans.insert(k,SG);
                        G--;
                        k+=SG.size();
                    }
                }
            }
            k=0;
            while(Y+V>0){
                if(k==0){
                    if(Y>0){
                        ans = "Y"+ans;
                        Y--;
                        k++;
                    }
                    else{
                        ans = SV+ans;
                        V--;
                        k+=SV.size();
                    }
                }
                else{
                    while(ans[k]=='Y'||ans[k-1]=='Y'||ans[k]=='O'||ans[k-1]=='O'||ans[k]=='G'||ans[k-1]=='G')k++;
                    if(Y>0){
                        ans.insert(k,"Y");
                        Y--;
                        k++;
                    }
                    else{
                        ans.insert(k,SV);
                        V--;
                        k+=SV.size();
                    }
                }
            }
        }
        else if(R+G == submax){
            while(R+G>0){
                if(R>0){
                    ans+="R";
                    R--;
                }
                else{
                    ans+=SG;
                    G--;
                }
            }
            k = 0;
            while(B+O>0){
                if(k==0){
                    if(B>0){
                        ans = "B"+ans;
                        B--;
                        k++;
                    }
                    else{
                        ans = SO+ans;
                        O--;
                        k+=SO.size();
                    }
                }
                else{
                    while(ans[k]=='V'||ans[k-1]=='V'||ans[k]=='B'||ans[k-1]=='B'||ans[k]=='G'||ans[k-1]=='G')k++;
                    if(B>0){
                        ans.insert(k,"B");
                        B--;
                        k++;
                    }
                    else{
                        ans.insert(k,SO);
                        O--;
                        k+=SO.size();
                    }
                }
            }
            k = 0;
            while(Y+V>0){
                if(k==0){
                    if(Y>0){
                        ans = "Y"+ans;
                        Y--;
                        k++;
                    }
                    else{
                        ans = SV+ans;
                        V--;
                        k+=SV.size();
                    }
                }
                else{
                    while(ans[k]=='Y'||ans[k-1]=='Y'||ans[k]=='O'||ans[k-1]=='O'||ans[k]=='G'||ans[k-1]=='G')k++;
                    if(Y>0){
                        ans.insert(k,"Y");
                        Y--;
                        k++;
                    }
                    else{
                        ans.insert(k,SV);
                        V--;
                        k+=SV.size();
                    }
                }
            }

        }
        else{
            while(Y+V>0){
                if(Y>0){
                    ans+="Y";
                    Y--;
                }
                else{
                    ans+=SV;
                    V--;
                }
            }
            k = 0;
            while(B+O>0){
                if(k==0){
                    if(B>0){
                        ans = "B"+ans;
                        B--;
                        k++;
                    }
                    else{
                        ans = SO+ans;
                        O--;
                        k+=SO.size();
                    }
                }
                else{
                    while(ans[k]=='V'||ans[k-1]=='V'||ans[k]=='B'||ans[k-1]=='B'||ans[k]=='G'||ans[k-1]=='G')k++;
                    if(B>0){
                        ans.insert(k,"B");
                        B--;
                        k++;
                    }
                    else{
                        ans.insert(k,SO);
                        O--;
                        k+=SO.size();
                    }
                }
            }
            while(R+G>0){
                if(k==0){
                    if(R>0){
                        ans = "R"+ans;
                        R--;
                        k++;
                    }
                    else{
                        ans = SG+ans;
                        G--;
                        k+=SG.size();
                    }
                }
                else{
                    while(ans[k]=='O'||ans[k-1]=='O'||ans[k]=='V'||ans[k-1]=='V'||ans[k]=='R'||ans[k-1]=='R')k++;
                    if(R>0){
                        ans.insert(k,"R");
                        R--;
                        k++;
                    }
                    else{
                        ans.insert(k,SG);
                        G--;
                        k+=SG.size();
                    }
                }
            }
        }            
        cout << ans << endl;
        */
        
        while(min(B+O,R+G)>0){
            if(B>0){
                ans+="B";
                B--;
            }
            else{
                ans+=SO;
                O--;
            }
            if(R>0){
                ans+="R";
                R--;
            }
            else{
                ans+=SG;
                G--;
            }
        }
        //BR
        if(B+O==0){
            while(min(R+G,Y+V)>0){
                if(Y>0){
                    ans+="Y";
                    Y--;
                }
                else{
                    ans+=SV;
                    V--;
                }
                if(R>0){
                    ans+="R";
                    R--;
                }
                else{
                    ans+=SG;
                    G--;
                }
            }
            //BRYR
            if(R+G==0){
                
                //Y
                int k = 0;
                while(Y+V>0){
                    if(k==0){
                        if(Y>0){
                            ans = "Y"+ans;
                            Y--;
                            k++;
                        }
                        else{
                            ans = SV+ans;
                            V--;
                            k+=SV.size();
                        }
                    }
                    while(ans[k]=='Y'||ans[k-1]=='Y'||ans[k]=='O'||ans[k-1]=='O'||ans[k]=='G'||ans[k-1]=='G')k++;
                    if(Y>0){
                        ans.insert(k,"Y");
                        Y--;
                        k++;
                    }
                    else{
                        ans.insert(k,SV);
                        V--;
                        k+=SV.size();
                    }
                }
            }
            else{
                
                /*
                int k = 1;
                while(R+G>0){
                    while(ans[k]=='O'||ans[k-1]=='O'||ans[k]=='V'||ans[k-1]=='V'||ans[k]=='R'||ans[k-1]=='R')k++;
                    if(R>0){
                        ans.insert(k,"R");
                        R--;
                        k++;
                    }
                    else{
                        ans.insert(k,SG);
                        G--;
                        k+=SG.size();
                    }
                }
                */
            }
        }
        //BR
        else{
            while(min(B+O,Y+V)>0){
                if(B>0){
                    ans+="B";
                    B--;
                }
                else{
                    ans+=SO;
                    O--;
                }
                if(Y>0){
                    ans+="Y";
                    Y--;
                }
                else{
                    ans+=SV;
                    V--;
                }
            }
            //BRBY
            if(B+O==0){
                //Y
                int k = 1;
                while(Y+V>0){
                    while(ans[k]=='Y'||ans[k-1]=='Y'||ans[k]=='O'||ans[k-1]=='O'||ans[k]=='G'||ans[k-1]=='G')k++;
                    if(Y>0){
                        ans.insert(k,"Y");
                        Y--;
                        k++;
                    }
                    else{
                        ans.insert(k,SV);
                        V--;
                        k+=SV.size();
                    }
                }
            }
            else{
                //B
            }   
        }
        cout << ans << endl;
            

            
    }
    return 0;
}

