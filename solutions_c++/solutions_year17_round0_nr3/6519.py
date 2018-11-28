#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

class stall {
public:
	unsigned long index, Ls, Rs;
	int left_big, full;
	stall() {
		index = Ls = Rs = 0;
		left_big = 1;
		full = 0;
	}
	stall(unsigned long i, unsigned long l, unsigned long r) {
		index = i;
		Ls = l;
		Rs = r;
		left_big = (l>r)? 1 : 0;
		full = 0;
	}
	stall(const stall &dest) {
		index = dest.index;
		Ls = dest.Ls;
		Rs = dest.Rs;
		left_big = dest.left_big;
	}
	void update(stall dest) {
		index = dest.index;
		Ls = dest.Ls;
		Rs = dest.Rs;
		left_big = dest.left_big;
	}
	void update(unsigned long i, unsigned long l, unsigned long r) {
		index = i;
		Ls = l;
		Rs = r;
		left_big = (l>r)? 1 : 0;
	}
};

int main() {
	int case_num;
	unsigned long N, K, min_val, max_val, i;
	stall* bathroom;
	stall *max;
	string tmp;

	// Parse in total number of cases
	getline(cin,tmp);
	case_num = stoi(tmp);

#ifdef DEBUG
	cout << "case_num : " << case_num << endl;		// Check case number count
#endif

	// Iterate through each case
	for (int count=1; count<=case_num; count++) {
		scanf("%lu %lu\n", &N, &K);

		if (N == K) {
			printf("Case #%d: 0 0\n",count);
			continue;
		}

		bathroom = new stall[N]();					// Initialize bathroom
		for (i=0;i<N;i++) {
			bathroom[i].update(i,i,N-1-i);
		}









		while (K > 0) {								// Iterate through K users
#ifdef DEBUG
			printf("K = %lu\n", K);
#endif
			max = new stall(0,0,0);

			for (i=0;i<N;i++) {						// Find best position
				if (!bathroom[i].full) {
					min_val = bathroom[i].left_big * bathroom[i].Rs + (1-bathroom[i].left_big) * bathroom[i].Ls;
					max_val = bathroom[i].left_big * bathroom[i].Ls + (1-bathroom[i].left_big) * bathroom[i].Rs;
#ifdef DEBUG
					printf("%lu : %lu %lu, left_big : %d, full : %d\n",
							bathroom[i].index,bathroom[i].Ls,bathroom[i].Rs,bathroom[i].left_big,bathroom[i].full);
					printf("------min_val : %lu, max_val : %lu--------\n", min_val, max_val);
#endif
					if (min_val > max->Ls || (min_val == max->Ls && max_val > max->Rs)) {
						max->update(bathroom[i].index,min_val,max_val);
					}
#ifdef DEBUG
					printf(">>>>> max : %lu : %lu %lu\n",max->index,max->Ls,max->Rs);
#endif
				}
			}







#ifdef DEBUG
			printf("\nBegin update :\n");
#endif
			for (i=0;i<N;i++) {						// Insert & update Ls, Rs of other stalls
				if (i < max->index && (max->index-i-1 < bathroom[i].Rs)) {
#ifdef DEBUG
					printf("///// Case 1 : i = %lu /////\n", i);
#endif
					bathroom[i].update(bathroom[i].index,bathroom[i].Ls, max->index-i-1);
				}
				else if (i > max->index && (i-max->index-1 < bathroom[i].Ls)) {
#ifdef DEBUG
					printf("///// Case 2 : i = %lu /////\n", i);
#endif
					bathroom[i].update(bathroom[i].index,i-max->index-1,bathroom[i].Rs);
				}
				else if (i == max->index) {
#ifdef DEBUG
					printf("///// Case 3 : i = %lu /////\n", i);
#endif
					bathroom[i].full = 1;
				}
			}

			K--;									// Update K
#ifdef DEBUG
			printf("===============================\n");
#endif
		}

#ifdef DEBUG
		printf("\nFinal state :\n");
		for (i=0;i<N;i++) {
			printf("%lu : %lu %lu\n",bathroom[i].index,bathroom[i].Ls,bathroom[i].Rs);
		}
		printf("===============================\n");
		printf("===============================\n");
#endif

		max_val = max->Rs;								// Retrieve final results
		min_val = max->Ls;
		printf("Case #%d: %lu %lu\n",count,max_val,min_val);		// print output
	} // end for (case)

	return 0;
}
