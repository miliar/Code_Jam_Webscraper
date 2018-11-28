#include <bits/stdc++.h>
using namespace std;

int N, K;
int status[2005], start_ind[2005], end_ind[2005];
int curr_ind, temp_ind, left_sec, right_sec, temp;

void reset()
{
	for(int i = 1; i <= 2 * N + 1; i++) {
	    status[i] = 0;
	    start_ind[i] = 0;
	    end_ind[i] = 0;
	}
}

int find()
{
	int ind, max = -1;
	for(int i = 1; i <= 2 * N + 1; i++) {
		//printf("%d ", status[i]);
	    if(max < status[i]) {
	    	max = status[i];
	    	ind = i;
	    }
	}
	//status[ind] = 0;
	//printf("\n");
	return ind;
}

int main()
{
	freopen("C-small-1-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test, tc, i;
	scanf("%d", &test);
	for(tc = 1; tc <= test; tc++)
	{
		reset();
		scanf("%d %d", &N, &K);
		curr_ind = N;
		temp_ind = N * 2;
		start_ind[N * 2 - 1] = start_ind[N * 2] = 1;
		end_ind[N * 2 - 1] = end_ind[N * 2] = N;
		for(i = 1; i <= K; i++)
		{
			if(i != 1) {
			    if(temp_ind % 2 == 1) {
				    curr_ind = (start_ind[temp_ind] + end_ind[temp_ind]) / 2;
				    //printf("1 = %d\n", curr_ind);
			    }
			    else if(temp_ind % 2 == 0) {
				    curr_ind = (start_ind[temp_ind] + end_ind[temp_ind]) / 2;
				    //printf("0 = %d\n", curr_ind);
			    }
		    }
		    else {
		    	if(curr_ind % 2) {
				    curr_ind = curr_ind / 2 + 1;
			    }
			    else {
				    curr_ind = curr_ind / 2;
			    }
		    }
			left_sec = curr_ind * 2 - 1;
			right_sec = curr_ind * 2;
			temp = 2 * curr_ind;
			//printf("%d %d %d %d\n", curr_ind, left_sec, right_sec, temp_ind);
			status[left_sec] = curr_ind - start_ind[temp_ind];
			status[right_sec] = end_ind[temp_ind] - curr_ind;
			
			start_ind[left_sec] = start_ind[temp_ind];
			end_ind[left_sec] = curr_ind - 1;
			start_ind[right_sec] = curr_ind + 1;
			end_ind[right_sec] = end_ind[temp_ind];
			//printf("%d %d %d %d\n", start_ind[left_sec], end_ind[left_sec], start_ind[right_sec], end_ind[right_sec]);
			
			status[temp_ind] = 0;
			temp_ind = find();
			//printf("ind : %d %d\n", curr_ind, temp_ind);
			//printf("%d %d\n", status[left_sec], status[right_sec]);
		}
		printf("Case #%d: %d %d\n", tc, status[right_sec], status[left_sec]);
	}
	return 0;
}
