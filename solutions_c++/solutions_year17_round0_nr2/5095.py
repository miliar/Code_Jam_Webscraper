#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<string>
#include<cmath>
#include<climits>
#include<fstream>
#include<sstream>

#define forn(i,n) for(int i=0;i<n;i++)
#define forv(it,v,type) for(vector<type>::iterator it=v.begin();it!=v.end();it++)

using namespace std;
ifstream fin ("input.in");
ofstream fout ("output.out");

string convert(string s,int index){
    s[index]--;
    for(int i=index+1;i<s.length();i++)
    {
     s[i]='9';
    }
    return s;
}
int main(){
    int T;
    fin >> T;
    forn(i,T)
    {
        string s;
    fin >> s;
    vector<int> eq;
    forn(j,s.length()-1)
    {
        if(s[j]>s[j+1]){
                        bool stop = false;
                        int backtrack=j;
                        while(!stop&&!eq.empty())
                        {   int next = eq.back();
                            eq.pop_back();
                            if(backtrack == next+1)
                            {
                            backtrack=next;
                            }
                            else{ stop = true;}
                        }
                        s=convert(s,backtrack);
                       }
        else if(s[j]==s[j+1])eq.push_back(j);
    }
    fout << "Case #" << i+1 << ": ";
    forn(j,s.length())
    {
    if(s[j]!='0')fout << s[j];
    }
    fout << endl;
    }
}
