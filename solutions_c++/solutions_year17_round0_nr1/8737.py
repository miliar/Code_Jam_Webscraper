#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <set>

typedef unsigned int uint;
using namespace std;

bool equals(const string& s1,const string& s2)
{
    
    for(uint i=0;i<s1.size();i++)
    {
        if(s1[i]!=s2[i]) return false;
    }
    return true;
}

void flip(string & s,uint pos,uint k)
{
    for(uint i=pos;i<(pos+k);i++)
    {
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}

set<string> history;
set<string> level;
bool found_solution=false;

bool has_key(const set<string>& myset,const string& s)
{
    return myset.find(s)!=myset.end();
}

set<string> generate_variants(const string& current,uint k)
{
    set<string> ret;
    for(uint i=0;i<=(current.size()-k);i++)
    {
        string variant(current);
        flip(variant,i,k);
        if(!has_key(history,variant)){
            history.insert(variant);
            ret.insert(variant);
        }
    }
    return ret;
}


bool cycle(const string& destination,uint k)
{
    set<string> copy(level);
    for(auto& s : copy)
    {
        //cout<<"In level "<<s<<endl;
        set<string> variants = generate_variants(s,k);
        level.insert(variants.begin(),variants.end());
        level.erase(s);
    }
    if(has_key(level,destination))
    {
        found_solution=true;
        return false;
    }
    return level.size()!=0;
}


int main(int argc,char ** argv)
{
    uint T;
    string S;
    uint K;
    uint casen=0;
    
    cin>>T;
    
    while(T)
    {
        history.clear();
        level.clear();
        found_solution=false;
        
        casen++;
        
        cin>>S>>K;
        
        //cout << "T="<< T<<" S="<<S<<" K="<<K<<endl; 
        
        
        uint flips = 0;
        
        if(S.find('-')==string::npos)
        {
            found_solution=true;
        }
        else
        {
            string solution(S.size(),'+');
            history.insert(solution);
            level.insert(solution);
            
            while(cycle(S,K))
            {
                flips++;
            }
            flips++;
        }
        
        cout<<"Case #"<<casen<<": ";
        if(found_solution)
        {
            cout<<flips<<endl;
        }
        else
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        
        T--;
    }
    
    return 0;
}