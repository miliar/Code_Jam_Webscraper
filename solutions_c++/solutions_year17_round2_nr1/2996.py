//
//  main.cpp
//  GoogleCodeJam
//
//  Created by yujian liu on 4/6/17.
//  CopyRb © 2017 yujian liu. All Rbs reserved.
//
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int testtidy(int n)
{
    int temp=0,max=n%10;
    while(n>0)
    {
        temp=n%10;
        if(max<temp)
            return 0;
        max=temp;
        n=n/10;
    }
    return 1;
}

void TidyNums()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin >> n;
        cout<<"Case #"<<i+1<<": ";
        if(n<10)
        {
            cout<<n<<endl;
        }
        else
        {
            for(int i=n;i>0;i--)
            {
                if(testtidy(i)==1)
                {cout<< i <<endl;
                    break;}
            }
        }
        
    }
}

void TidyNums_large()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        string s;
        cin >> s;
        cout << "Case #"<<i+1<<": ";
        int len = s.size();
        if(len==1)
            {
                cout<<s<<endl;
            }
        else
        {
            
            for(int j=len-2;j>=0;j--)
            {
                if(s[j]>s[j+1])
                {
                    s[j]-=1;
                    for(int k=j+1;k<len;k++)
                    {s[k]='9';}
                }
            }
            while(s[0]=='0')
            {
                s.erase(s.begin());
            }
            cout << s<<endl;
        }
    }
}
void Bathroom_Stalls()
{
    int t;
    cin >> t;
    for(int i = 0;i < t;i++)
    {
        int n, k;
        cin >> n >> k;
        for(int i=0;i<t;i++)
        {
            cout << "Case #"<<i+1<<": ";
            
        }
        
        
    }
}
void oversize_Pancake_Oven()
{
    ofstream myfile;
    myfile.open("/Users/yujianliu/Downloads/sub-1.out");
    int t, n, m, flag=0;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for(auto i=0;i<t;i++)
    {
        string s;
        int res=0;
        cin >> s >> n;
        for(m=0;m<=s.size()-n;m++)
        {
            if(s[m]=='-')
            {
                res++;
                for(int k=0;k<n;k++)
                {
                    if(s[k+m]=='-')
                    {s[k+m]='+';}
                    else
                    {s[k+m]='-';}
                }
            }
        }
        myfile <<"Case #"<<i+1<<": ";
        while(m<s.size())
        {
            if(s[m]=='-')
            {
                flag=1;
            }
            m++;
        }
        m=0;
        if(flag==1)
        {
            myfile<<"IMPOSSIBLE"<<endl;
        }
        else
            myfile<<res<<endl;
        res=0;
        flag =0;
    }
}
void oversize_Pancake_Oven_opt()
{
    ifstream input;
    ofstream output;
    input.open("/Users/yujianliu/Downloads/A-large-practice (3).in");
    output.open("/Users/yujianliu/Downloads/sub-1.out");
    int t;
    input >> t;
    for(int i=1;i<=t;i++)
    {
        string s;
        int n;
        input >> s >> n;
        int len = s.size(),flip_count=0, res=0;
        vector<int> memo(len,0);
        
        output << "Case #"<<i <<": ";
        for(int j=0;j<len;j++)
        {
            flip_count+=memo[j];
            memo[j]=flip_count;
            if((s[j]=='-'&&flip_count%2==0)||(s[j]=='+'&&flip_count%2!=0))
            {
                if(j<len-n+1)
                {
                    flip_count++;
                    res++;
                    if(j<len-n)
                    memo[j+n]-=1;
                }
                else
                {
                    output << "IMPOSSIBLE" <<endl;
                    break;
                }
                
            }
            memo[j]=flip_count;
            if(j==len-1)
            output<< res <<endl;
        }
        
    }
    input.close();
    output.close();
}

void bathroom_Stalls_1()
{
    ifstream input;
    ofstream output;
    input.open("/Users/yujianliu/Downloads/C-small-practice-1.in");
    output.open("/Users/yujianliu/Downloads/sub-1.out");
    int t;
    input >> t;
    for(int i=1;i<=t;i++)
    {
        int n, k;
        input >> n >> k;
        set<int> stalls_Occupied;
        stalls_Occupied.insert(0);
        stalls_Occupied.insert(n+1);
        output << "Case #"<< i <<": ";
        for(int i=0;i<k;i++)
        {
            int min_Dis=0, max_Dis=0, index=0;
            for(int j=1;j<=n;j++)
            {
                auto it = stalls_Occupied.find(j);
                if(it==stalls_Occupied.end())
                {
                    int Lb = *(--stalls_Occupied.lower_bound(j)), Rb = *stalls_Occupied.upper_bound(j);
                    if(min_Dis<min(j-Lb,Rb-j))
                    {
                        min_Dis = min(j-Lb,Rb-j);
                        index = j;
                    }
                    else if(min_Dis == min(j-Lb,Rb-j))
                    {
                        if(max_Dis < max(j-Lb,Rb-j))
                        {
                            max_Dis = max(j-Lb,Rb-j);
                            index = j;
                        }
                    }
                }
            }
            stalls_Occupied.insert(index);
            if(i==k-1)
                output<< max_Dis-1 << " "<<min_Dis-1<<endl;
        }
        
    }
    
    input.close();
    output.close();

}

void Alphabet_Cake()
{
    ifstream input;
    ofstream output;
    input.open("/Users/yujianliu/Downloads/A-small-attempt1.in");
    output.open("/Users/yujianliu/Downloads/sub-1.out");
    int t;
    input >> t;
    for(int i=1;i<=t;i++)
    {
        int R,C;
        input >> R >>C;
        vector<char> row(C,0);
        vector<vector<char>> cake(R,row);
        for(int j=0;j<R;j++)
        {
            for(int k=0; k<C;k++)
                input >> cake[j][k];
        }
        output << "Case #"<< i << ": "<<endl;
        for(int j=0;j<R;j++)
        {
            for(int k=0; k<C;k++)
            {
                if(cake[j][k]!='?')
                {
                    for(int m=j+1;m<R&&cake[m][k]=='?';m++)
                    {
                        cake[m][k]=cake[j][k];
                    }
                    if(j>0&&cake[j-1][k]=='?')
                    {
                        for(int m=0;m<j;m++)
                        {
                            cake[m][k]=cake[j][k];
                        }
                    }
                }
            }
        }
        for(int j=0;j<R;j++)
        {
            for(int k=0;k<C;k++)
            {
                if(cake[j][k]=='?')
                {
                    int m=k;
                    for(;m<C&&cake[j][m]=='?';m++);
                    if(m==C)
                    {
                        for(m=k;m>0&&cake[j][m]=='?';m--);
                        while(k>m)
                        {
                            cake[j][k] = cake[j][m];
                            k--;
                        }
                    }
                    else
                    {
                        while (k<m) {
                            cake[j][k] = cake[j][m];
                            k++;
                        }
                    }
                }
                
            }
            for(int s=0;s<C;s++)
                output<<cake[j][s]<<" ";
            output<< endl;
        }
    }
    input.close();
    output.close();
}

void Ratarouille()
{
    ifstream input;
    ofstream output;
    input.open("/Users/yujianliu/Downloads/A-small-attempt1.in");
    output.open("/Users/yujianliu/Downloads/sub-1.out");
    int t;
    input >> t;
    for(int i=1;i<=t;i++)
    {
        int N,P;
        input >> N >> P;
        vector<int> ingredients(N,0);
        vector<vector<int>> packages(P,ingredients);
        
        int res=0;
        output << "Case #"<<i<<": ";
        for(int j=0;j<N;j++)
        {
            input >> ingredients[j];
        }
        for(int k=0;k<N;k++)
        {
            for(int j=0;j<P;j++)
            {
                input >> packages[j][k];
            }
        }
        for(int j=0;j<P;j++)
        {
            float maxlb=0;
            float minub=__FLT_MAX__;
            for(int k=0;k<N;k++)
            {
                maxlb=maxlb > packages[j][k]/(ingredients[k]*1.1) ? maxlb : packages[j][k]/(ingredients[k]*1.1);
                minub=minub < packages[j][k]/(ingredients[k]*0.9) ? minub : packages[j][k]/(ingredients[k]*0.9);
            }
            if(maxlb<minub)
                res++;
        }
        output<<res<<endl;
    }
    input.close();
    output.close();
}

void Cruise_Control()
{
    ifstream input;
    ofstream output;
    input.open("/Users/yujianliu/Downloads/A-large (1).in");
    output.open("/Users/yujianliu/Downloads/sub-1.out");
    int t;
    input>>t;
    for(int i=1;i<=t;i++)
    {
        output<<"Case #"<< i<<": ";
        int D,N;
        input>>D>>N;
        double maxtime=0;
        for(int i=0;i<N;i++)
        {
            int dis,sp;
            input >> dis >>sp;
            maxtime= (double)(D-dis)/sp < maxtime ? maxtime : (double)(D-dis)/sp;
        }
        double res = D/maxtime;
        output<<fixed<<setprecision(6);
        output<<  res<<endl;
    }
    input.close();
    output.close();
}
int main() {
    Cruise_Control();
        return 0;
}
