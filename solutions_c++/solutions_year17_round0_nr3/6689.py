/*	Problem
	A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. 
	The other N stalls are for users.

	Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they 
	follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S 
	and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, 
	that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those 
	where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

	K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

	When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?
*/

/*Input 
	5
	4 2
	5 2
	6 2
	1000 1000
	1000 1
*/

/*OUTPUT
	Case #1: 1 0
	Case #2: 1 0
	Case #3: 1 1
	Case #4: 0 0
	Case #5: 500 499
*/

#include <iostream>
#include <vector>
using namespace std;

struct Pair
{
	int f, l;
};

const int n = 9;

vector<bool> v(n, 0);

Pair heart(){ // It will give me pair, such that f and l of that pair will denote largest unoccupied sequence of br's
	int base = 0, jump = base + 1;
	int ls1 = v.size() - 1;
	int maxF = base, maxL = ls1;
	int maxfound = 0;
	int currCnt = 0;
	while(1){
		if(v[jump] == 1){
			//cout << "entered If clause "<<endl;
			currCnt = jump - base - 1;
			if(currCnt >= maxfound){
				maxF = base;
				maxL = jump;
				maxfound = currCnt;
				//cout << "jump = " << jump << endl;
				//cout << "ls1 = " << ls1 << endl;
			}
			currCnt = 0;
			base = jump;
			jump = base + 1;
		}
		else{
			currCnt++;
			jump++;
		}
		if(jump > ls1) break;
		
	}
	//cout << "exiting heart, maxF = " << maxF << " maxL = " << maxL <<endl;
	return {maxF, maxL};
}

Pair core(int ii){
	while(ii > 1){
		Pair coo = heart();
		int fir = coo.f, sec = coo.l, chng = (fir + sec) / 2;
		v[chng] = 1;
		//cout << "placed in " << chng << endl;
		ii--;
	}
	Pair coo = heart();
	int fir = coo.f, sec = coo.l, chng = (fir + sec) / 2;
	int ll = sec - chng - 1;
	int rr = chng - fir - 1;
	return {ll, rr};
}

void rsz(int m){
	while(!v.empty()){
		v.pop_back();
	}
	v.push_back(1);
	m--;
	while(m > 1){
		v.push_back(0);
		m--;
	}
	v.push_back(1);
	return;
}

int main(){
	int T;
	cin >> T;
	
	std::vector<Pair> v1;
	for(int i = 1; i <= T; i++){
		int n, k;
		cin >> n >> k;
		v1.push_back({n, k});
		//cout << n << ", " << k << " received." << endl;
	}
	//cout << "input done!" << endl;
	for(int i = 0; i < T; i++){
		int n = v1[i].f, k = v1[i].l; 
		rsz(n + 2);
		Pair pp = core(k);
		//cout << "core(" << k << ") called\n";
		cout << "Case #" << 1 + i << ": "<< pp.f << " " << pp.l << endl;
	}
}