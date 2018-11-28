#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
	long long unsigned N, K;
	int T, count = 1;

	freopen ("C-small-1-attempt0.in","r",stdin);
	freopen ("C-small-1-attempt0.out","w",stdout);

	cin >> T;	
	while(T-- > 0) {
	    cin >> N >> K; 
	    int arr[N+2] = {0}, Ls[N+2] = {0}, Rs[N+2] = {0}, left, right, min, max;
	    arr[0] = 1;
	    arr[N+1] = 1;
	    int maximum_element,maximum_element1;
	    for (int k = 0; k < K; ++k)
	    {

	    		// cal (ls,rs) pairs for each N
			    for (int i = 1; i < N+1; ++i)
			    {
			    	if(arr[i] == 1){
			    		Ls[i] = INT_MAX;
			    		Rs[i] = INT_MAX;
			    		continue;
			    	}
			    	//Left
			    	left = i-1;
			    	int ct = 0;
			    	while(left >= 0){
			    		if(arr[left] == 0){
			    			ct++;
			    			left--;
			    		}
			    		else{
			    			break;
			    		}
			    	}
			    	Ls[i] = ct;

			    	//Right
			    	right = i+1;	
			    	ct = 0;
			    	while(right < N+1) {
			    	    if(arr[right] == 0)
			    	    {
			    	    	ct++;
			    	    	right++;
			    	    }
			    	    else
			    	    	break;
			    	}
			    	Rs[i] = ct;
			    	
			    }

			    // choose i base on min(ls,rs)
			    int min[N+1] = {0};
			    vector<int> index;
			    for (int n = 1; n < N+1; ++n)
			    {
			    	if(arr[n] == 1)
			    		continue;
			    	if(Ls[n] < Rs[n]){
			    		min[n] = Ls[n];
			    	}
			    	else{
			    		min[n] = Rs[n];
			    	}
			    }

			    maximum_element = min[1];
			    for (int n = 2; n < N+1; ++n)
			    {
			    	if(arr[n] == 1)
			    		continue;
			    	if(maximum_element < min[n])
			    		maximum_element = min[n];
			    }

			    for (int n = 1; n < N+1; ++n)
			    {
			    	if(arr[n] == 1)
			    		continue;
			    	if(maximum_element == min[n])
			    		index.push_back(n);
			    }


					// choose i based on max(ls, rs)
				    int max[N+1] = {0};			    
				    for (int n = 1; n < N+1; ++n)
				    {
				    	if(arr[n] == 1)
			    			continue;
				    	if(Ls[n] < Rs[n]){
				    		max[n] = Rs[n];
				    	}
				    	else{
				    		max[n] = Ls[n];
				    	}
				    }
				    maximum_element1 = max[index.front()];
				    vector<int> max_index;
				    for (vector<int>::iterator it = index.begin() ; it != index.end(); ++it){
			    		if(max[*it] > maximum_element1){
			    			maximum_element1 = max[*it];
			    		}				    		
			    	}



			    if (index.size() == 1)
			    {
			    	arr[index.front()] = 1;
			    }
			    else{

			    	
			    	for (vector<int>::iterator it = index.begin() ; it != index.end(); ++it){
			    		if(maximum_element1 == max[*it]){
			    			max_index.push_back(*it);
			    		}				    		
			    	}

			    	arr[max_index.front()] = 1;
			    }

			    

		}
	    cout << "Case #" << count++ <<": " << maximum_element1 << " " << maximum_element << endl;
	}
	return 0;
}