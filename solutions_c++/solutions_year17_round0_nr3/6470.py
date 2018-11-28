#include <iostream>
using namespace std;

int result_min;
int result_max;

int max(int a, int b){
	if (a > b) return a;
	else return b;
}

int min(int a, int b){
	if (a < b) return a;
	else return b;
}

struct room{
	int pos;
	int min;
	int max;
};

int distancehelper(int* s,int pos,char d){
	int rsf = 0;
	switch(d){
		case 'l':
		do{ 
			pos--;
			rsf ++;
		} while(s[pos] != 1);
		break;
		case 'r':
		do{ 
			pos++;
			rsf ++;
		} while(s[pos] != 1);
		break;
	}
	return rsf-1;
}

void findstall(int* s,int num_stalls,int status = 0){
	struct room best[num_stalls];
	int room_ptr = 0;
	int min_sofar = 0;
	int max_sofar = 0;
	for (int i = 1;i<num_stalls+1;i++){
		if (s[i] == 1) continue;
		int temp_left = distancehelper(s,i,'l');
		int temp_right = distancehelper(s,i,'r');
		best[room_ptr].pos = i;
		best[room_ptr].min = min(temp_left,temp_right);
		best[room_ptr].max = max(temp_left,temp_right);
		if (best[room_ptr].min > min_sofar) min_sofar = best[room_ptr].min;
		room_ptr ++;
	}
	struct room secondbest[num_stalls];
	int room_ptr_2=0;
	for (int i=0;i<room_ptr;i++){
		if (best[i].min == min_sofar){
			secondbest[room_ptr_2] = best[i];
			if (best[i].max > max_sofar) max_sofar = best[i].max;
			room_ptr_2++;
		}
	}
	if (room_ptr_2 == 1){
		s[secondbest[0].pos] = 1;
		if (status ==1 ){
			result_max = secondbest[0].max;
			result_min = secondbest[0].min;
		}
	}
	struct room thirdbest[num_stalls];
	int room_ptr_3 = 0;
	for (int i = 0;i<room_ptr_2;i++){
		if (secondbest[i].max == max_sofar){
			thirdbest[room_ptr_3] = secondbest[i];
			room_ptr_3++;
		}
	}

	s[thirdbest[0].pos] = 1;
	if (status ==1 ){
		result_max = thirdbest[0].max;
		result_min = thirdbest[0].min;
	}
}


void stall(int num_stalls, int num_users){

	
	int stalls[num_stalls+2];

	// stalls initialize
	for (int i = 1; i<num_stalls+1;i++)
		stalls[i] = 0;
	stalls [0] = 1;
	stalls [num_stalls+1] = 1;

	// users searching
	for (int i =0; i< num_users; i++){
		if (i == num_users -1){
			findstall(stalls,num_stalls,1);
		} else {
			findstall(stalls,num_stalls,0);
		}
	}
}

int main(){

	int t;
	int num_stalls;
	int num_users;
	cin >> t;
	for (int i =0;i<t;i++){
		cin >> num_stalls >> num_users;
		stall(num_stalls,num_users);
		cout <<"Case #" << i+1 << ": " << result_max << " " << result_min;
		cout << endl;
	}
	return 0;
}