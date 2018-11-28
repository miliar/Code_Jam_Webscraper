#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        int n,k;
        cin >> n >> k;
        int a[100001],x=0,y=1;
        a[x]=n;
        while(1){
            a[y]=a[x]/2;
            a[y+1]=a[x]%2==0?a[x]/2-1:a[x]/2;
            if(!a[y]&&!a[y+1]&&!a[x+1])
                break;
            x++;
            y+=2;
        }
        sort(a,a+y);
        reverse(a,a+y);
        cout << "Case #" << i << ": ";
        cout << a[k-1]/2 << " ";
        a[k-1]%2==0?cout << a[k-1]/2-1:cout << a[k-1]/2;
        cout << endl;
    }
    return 0;
}
