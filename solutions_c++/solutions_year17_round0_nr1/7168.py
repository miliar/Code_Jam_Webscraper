#include <iostream>
#include <string>
using namespace std;

char data[1001];

int main()
{
    int n,k;
    cin >> n;
    for(int i{0};i<n;++i)
    {
        cin >> data;
        cin >> k;
        int j{ 0 },r{ 0 };
        for(;j<1001;++j) {
            if( !data[ j + k - 1 ] ) {
                break;
            }
            if( data[j]=='-' ) {
                ++r;
                for(int w{0};w<k;++w)
                    data[j+w] = data[j+w]=='+'?'-':'+';
            }
            data[j] = '\0';
        }
        bool imp = false;
        while(data[j]) {
            if( data[j] == '-') {
                imp = true;
            }
            data[j]='\0';
            ++j;
        }
        if( imp )
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<r<<endl;
    }
}
