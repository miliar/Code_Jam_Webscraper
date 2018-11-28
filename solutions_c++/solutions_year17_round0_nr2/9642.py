#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int main()
{
    freopen( "B-small-attempt12.in", "r", stdin );
	freopen( "output.out", "w", stdout );
    int x,y,z,a,m,max=0;
    cin>>x;
    for(int i=0;i<x;i++){
        cin>>y;
        max=0;
        for(int i=1;i<=y;i++){
        int c=11,m=0;
        a=i;
        while(a>0){
            z=a%10;
            if(z>c){
                c=11;
                m=1;
                continue;
            }
            c=z;
            a=a/10;

        }
        if(max<i&&m==0){
            max=i;
        }
        }
        cout<<"Case #"<<i+1<<": "<<max<<endl;

    }
    return 0;
}
