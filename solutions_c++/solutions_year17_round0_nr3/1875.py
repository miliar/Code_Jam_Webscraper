#include<iostream>
#include<string>
#include<queue>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
long long heap[5];
long long value[5];
int heap_size;
void max_extract(){
    if( heap_size == 3 ){
        if( heap[2] > heap[3] ){
            heap[1] = heap[2];
            value[1] = value[2];
            heap[2] = heap[3];
            value[2] = value[3];
        }
        else{
            heap[1] = heap[3];
            value[1] = value[3];
        }
    }
    else if( heap_size == 2 ){
        heap[1] = heap[2];
        value[1] = value[2];
    }
    if( heap_size > 0 ){
        heap_size--;
    }
}
void insert_value( long long num, long long val ){
    int i;
    for( i = 1; i <= heap_size ; i++ ){
        if( heap[i] == num ){
            value[i] = value[i] + val;
            break;
        }
    }
    if( i > heap_size ){
        heap_size++;
        heap[heap_size] = num;
        value[heap_size] = val;
        if( heap[heap_size] > heap[1] ){
            heap[3] = heap[1];
            value[3] = value[1];
            heap[1] = num;
            value[1] = val;
        }
    }
}
int main(){
    int testcase;
    long long n,k,sum,a,b,c,ret,val,ans;
   // freopen("input.txt","r",stdin);
   // freopen("output.txt","w",stdout);
    scanf("%d",&testcase);
    for( int t = 1; t <= testcase; t++ ){
        scanf("%lld%lld",&n,&k);
        heap_size = 0;
        insert_value(n,1);
        sum = 0;
        while( true ){
            ret = heap[1];
            val = value[1];
            k = k - val;
            if(  k <= 0 ){
                ans = ret;
                break;
            }
            max_extract();
            if( ret%2 == 0 ){
                ret = ret/2;
                insert_value(ret,val);
                ret--;
                insert_value(ret,val);
            }
            else{
                ret = ret/2;
                if( ret > 0 ){
                    val = val*2;
                    insert_value(ret,val);
                }
                else{
                    ans = 1;
                    break;
                }
            }

        }
        a = ans/2;
        b = a;
        if( ans%2 == 0){
            b--;
        }
        printf("Case #%d: %lld %lld\n",t,a,b);
    }

return 0;
}
