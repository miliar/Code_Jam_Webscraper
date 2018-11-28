#include <iostream>
#include <stdio.h>
#include <vector>
#include <cstdlib>

using namespace std;

#define AmanJain jainaman224

int compare(const void *a, const void *b){
    if(*(long *)a > *(long *)b)
        return 1;
    if(*(long *)a < *(long *)b)
        return -1;
    return 0;
}

void scanlonglong(long long &x){
    register long long c=getchar_unlocked();
    x=0;
    for(;(c<48 || c>57);
    	c=getchar_unlocked());
    for(;c>47 && c<58;c=getchar_unlocked()){
        x=(x<<1)+(x<<3)+c-48;
    }
}

void scanlong(long &y){
    register long d=getchar_unlocked();
    y=0;
    for(;(d<48 || d>57);
    	d=getchar_unlocked());
    for(;d>47 && d<58;d=getchar_unlocked()){
        y=(y<<1)+(y<<3)+d-48;
    }
}

int main(){
    int t, n, p, ans, i, j, k, l, m, flag, r;
    long a[50], b[50][50], lower, upper, c[50];
    cin >> t;
    for(i=1;i<=t;i++){
        for(j=0;j<50;j++)
            c[j]=0;
        ans = 0;
        cin >> n >> p;
        for(j=0;j<n;j++)
            cin >> a[j];
        for(k=0;k<n;k++){
            for(j=0;j<p;j++)
                cin >> b[k][j];
            qsort(b[k], p, sizeof(long), compare);
        }
        flag = 0;
        for(l=1;;l++){
            for(m=0;m<n;m++){
                if(float(b[m][c[m]])<(l*a[m])*0.9){
                    c[m]++;
                    if(c[m]>=p)
                        flag = 1;
                    l--;
                    break;
                }
                if(b[m][c[m]]>(l*a[m])*1.1)
                    break;
            }
            if(m==n){
                ans++;
                for(r=0;r<n;r++){
                    c[r]++;
                    if(c[r]>=p)
                        flag = 1;
                }
                l--;
            }
            if(flag)
                break;
        }

        cout << "CASE #" << i << ": " << ans << endl;
    }
	return 0;
}