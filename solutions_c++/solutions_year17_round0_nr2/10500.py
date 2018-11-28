#include <iostream>

using namespace std;

bool isTidy(int number)
{
    int a[10];
    int i = 0;

    while(number != 0) {
        a[i] = number % 10;
        number /= 10;
        i++;
    }

    for(int j = 0;j < i - 1;j++) {
        if(a[j+1] > a[j]) return false;
    }

    return true;
}

int main()
{
    int t, n, a[10000];

    cin >> t;

    for(int i = 0;i < t;i++) {
        cin>>a[i];
    }

    for(int i = 0;i < t;i++) {
        for(int j = a[i];j > 0;j--) {
            if(isTidy(j)) {
                cout<<"Case #"<<i+1<<": "<<j<<endl;
                break;
            }
        }
    }

    return 0;
}