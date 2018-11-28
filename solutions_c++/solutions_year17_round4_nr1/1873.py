#include <bits/stdc++.h> 

#define fi(a,b,c) for(int a=b; a<=c; a++) 
#define fii(a,b,c) for(int a=b; a<c; a++) 
#define fd(a,b,c) for(int a=b; a>=c; a--) 
#define pb push_back 
#define mp make_pair 
#define ft first 
#define sc second 


typedef long long ll; 
const int N = 1000; 

using namespace std; 

int n, p, cnt[5], ans ; 
int a[1000]; 
int query ; 

void solve2()  { 
	fi(i, 0, p) cnt[i]= 0; 
	fi(i, 1, n) cnt[a[i] % 2] ++; 
	int kt = cnt[0]; 
	kt += ceil((double)cnt[1] / 2.0); 
	ans = kt ; 
} 
void solve3() {
	fi(i, 0, p) cnt[i] = 0 ;  
	fi(i, 1, n) cnt[a[i] % 3] ++;  
	int kt = cnt[0];  
	if (cnt[1] > cnt[2]) { 
		kt += cnt[2];
		cnt[1] -= cnt[2]; 
		kt += (ceil((double)cnt[1] / 3.0)); 
	} else { 
		kt += cnt[1]; 
		cnt[2] -= cnt[1]; 
		kt += (ceil((double)cnt[2] / 3.0)); 
	}
	ans = kt; 

}; 
void solve4() {
	fi(i, 0, p) cnt[i] = 0 ;  
	fi(i, 1, n) cnt[a[i] % 3] ++;  
	int kt = cnt[0]; 
	kt += cnt[2] / 2; 
	cnt[2] %= 2;
	int kk = min(cnt[1], cnt[3]); 
	kt += kk ;  
	cnt[1] -= kk; 
	cnt[3] -= kk; 
	kk = max( cnt[1], cnt[3]);  
	if (cnt[2]) { 
		if (kk >= 2) 
			{ 
				kt ++; 
				kk -= 2;   
				kt += (ceil((double)kk / 4.0)); 
			}
		else { 
			kt ++; 
		}
	} else { 
		kt += (ceil((double)kk / 4.0));
	}
	ans = kt; 
}; 

int main() 
{
	
	freopen("A-small-attempt3.in", "r", stdin); 
	freopen("new_out.txt", "w", stdout); 
	scanf("%d", &query); 
	fi(t, 1, query) { 
		scanf("%d %d", &n, &p);  
		fi(i, 1, n) scanf("%d", &a[i]);  
		ans = 0; 
		if (p == 2)  solve2(); 
		else if (p == 3) solve3(); 
		else if (p == 4) solve4(); 
		printf("Case #%d: %d\n", t, ans); 
	}

}