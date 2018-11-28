#include <iostream>
#include <string>
using namespace std;


string input;
char output[20];
string max_s;

bool great( const std::string& a,
            const std::string& b)
{
    if(a.size() != b.size() ) {
        return a.size() > b.size();
    }
    //129 132
    for(int i{0};i<a.size();++i) {
        if( a[i]==b[i] ) continue;
        return a[i] > b[i];
    }
    return false;
}

void do_job(int idx,int n)
{
    if( great(output,input) ){
        return;
    }
    if( great(output, max_s) ) {
        max_s = output;
    }
    if( idx > input.size()-1 ) return;
    for(int i{ 9 };i>=n;--i) {
        output[idx] = i+'0';
        do_job( idx + 1, i);
        output[idx] = 0;
    }
}

int main()
{
    int n;
    cin >> n;
    for(int i{1};i<=n;++i)
    {
        cin >> input;
        for(int j{0};j<20;j++)
            output[j] = 0;
        do_job( 0, 1 );
        cout<<"Case #"<<i<<": "<<max_s<<endl;
        max_s.clear();
    }
}
