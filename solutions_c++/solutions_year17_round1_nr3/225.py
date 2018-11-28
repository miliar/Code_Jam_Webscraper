#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long
#define Ldouble long double
#define PI 3.1415926535897932384626

#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define fi first
#define se second

using namespace std;

int t, my_hp, my_atk, op_hp, op_atk, buff, debuff;
LL ans1, ans;

void upd(int u){
	//debuff u times, #rounds = ?
	LL ret = u + ans1;
	//direct sim :(
	int oa = op_atk, mh = my_hp;
	FI(i, 1, u){
		oa = max(0, oa - debuff); //debuff
		mh -= oa; //knight attack
		int na = max(0, oa - debuff);
		if(na >= mh && i == 1) return;
		if(na >= mh){
			ret++; //heal
			mh = my_hp - oa; //knight attack
		}
	}
	FI(i, 1, ans1){
		//my attack
		if(i == ans1) break;
		mh -= oa;
		if(oa >= mh && i < ans1 - 1){
			if(mh == my_hp - oa) return;
			ret++; //heal
			mh = my_hp - oa; //knight attack
		}
	}
	ans = min(ans, ret);
	return;
}

void solve(){
	//how many rounds are needed to defeat the fucking knight?
	//First, optimise the atk + buff portion
	ans1 = ceil((op_hp + .0) / my_atk);
	if(buff > 0){
		FI(i, 1, 32000){
			//i buffs
			ans1 = min(ans1, i + (LL)ceil((op_hp + .0) / (my_atk + 1LL * i * buff)));
		}
		FI(i, 1, 32000){
			//kill in i rounds
			int j = max(0, (int)ceil(((op_hp + .0) / i - my_atk) / buff));
			ans1 = min(ans1, (LL)i + j);
		}
	}
	
	if(ans1 == 1){ //special case: already good!
		printf("1\n");
		return;
	}
	
	ans = (1LL << 60);
	//Second, optimise the heal + debuff portion
	upd(0);
	if(debuff > 0){
		FI(i, 1, 32000){
			//wanna make heal interval >= i
			int j = max(0, (int)(floor((op_atk - (my_hp + .0) / i) / debuff) + 1));
			upd(j);
		}
		FI(i, 0, 32000){
			//wanna make op_atk <= i
			int j = max(0, (int)ceil((op_atk - i + .0) / debuff));
			upd(j);
		}
	}
	
	if(ans == (1LL << 60)) printf("IMPOSSIBLE\n");
	else printf("%lld\n", ans);
	return;
}
int main(){
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C1.out", "w", stdout);
	scanf("%d", &t);
	FI(i, 1, t){
		printf("Case #%d: ", i);
		scanf("%d %d %d %d %d %d", &my_hp, &my_atk, &op_hp, &op_atk, &buff, &debuff);
		if(op_atk - debuff >= my_hp && my_atk < op_hp){
			printf("IMPOSSIBLE\n");
			continue;
		}
		solve();
	}
	return 0;
}

