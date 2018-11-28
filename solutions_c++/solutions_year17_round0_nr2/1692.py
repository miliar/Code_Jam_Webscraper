#include <iostream>
#include <cassert>

using namespace std;

bool can_tidy(string &S,const char d,int i)
{
    while(i<S.size()) {
	if(S[i]>d)
	    return true;
	if(S[i]<d)
	    return false;
	i++;
    }
    return true;
}

void fill9(string &S,int i)
{
    while(i<S.size())
	S[i++]='9';
}

void tidy_down(string &S,int i)
{
    while(i<S.size()-1) {
	if(!can_tidy(S,S[i],i+1)) {
	    S[i]--;
	    assert(S[i]>='0');
	    fill9(S,i+1);
	    return;
	}
	i++;
    }
}

void test(int cse)
{
    cout<<"Case #"<<cse<<": ";
    string S; cin>>S;
    tidy_down(S,0);
    const char *s=S.c_str();
    while(*s=='0' && s[1])
	s++;
    cout<<s<<endl;
}

int main()
{
    int T; cin>>T;
    for(int i=0; i<T; i++)
	test(i+1);
    return 0;
}
