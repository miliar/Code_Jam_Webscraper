#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-small-attempt2.in","r",stdin) ;
	freopen("output.in","w",stdout) ;
	int count = 1 ;
	int t;
	cin>>t;
	while(t--){
		long long int n;
		scanf("%lld",&n) ;
		int size = 1 ;
		long long int temp = n ;
		int flag = 0 ;
		int prev = temp%10 ;;
		temp = temp/10 ;
		while( temp != 0 ){
			int rem = temp%10 ;
			if( prev < rem && flag == 0 ){
				flag = 1 ;
			}
			prev = rem ;
			temp = temp/10 ;
			size++ ;
		}
		if( flag == 0 ){
			cout<<"Case #"<<count<<": "<<n<<"\n";
			count++ ;
			continue ;
		}
		int a[size+1] ;
		temp = n ;
		int i = size-1 ;
		while( temp != 0 ){
			int x = temp%10 ;
			a[i--] = x ;
			temp /= 10 ;
		}
	/*	for( int i = 0 ; i < size ; i++ ){
			cout<<a[i]<<" ";
		}*/
		i = 0 ;
		flag = 0 ;
		while( i < size ){
			if( a[i] >= a[i+1] ){
				flag = 1 ;
				a[i] = a[i]-1 ;
				a[i+1] = 9 ;
				break ;
			}
			i++ ;
		}
		for( i = 0 ; i < size ; i++ ){
			if( a[i] > a[i+1] ){
				a[i+1] = 9 ;
			}
		}
		flag = 0 ;
		cout<<"Case #"<<count<<": ";
		count++ ;
		for( i = 0 ; i < size ; i++ ){
			if( a[i] == 0 && flag == 0 ){
				continue ;
			}
			if( a[i] != 0 ){
				flag = 1 ;
			}
			cout<<a[i];
		}
		cout<<"\n" ;
	}
}
