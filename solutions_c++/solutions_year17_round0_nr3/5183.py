# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("Cout_medium.txt", "w", stdout);
    int cases, caseno = 0;
    unsigned long long n, k, num, first, second;
    scanf ("%d", &cases);
    while(cases--){
        scanf("%llu %llu", &n, &k);

        priority_queue <unsigned long long> Q;
        Q.push(n);
        for (unsigned long long i=1; i<k && !Q.empty(); i++){
            num = Q.top();
            //cout << num << endl;
            Q.pop();
            first = second = (num-1)/2;
            if ((num-1)%2 != 0) first++;
            if (first) Q.push(first);
            if (second) Q.push(second);
        }
        if (!Q.empty()){
            num = Q.top();
            Q.pop();
            first = second = (num-1)/2;
            if ((num-1)%2 != 0) first++;
        }
        else first = second = 0;

        /// Needed for large datasets
        /**
        unsigned long long den= (1ULL<<((int)floor(log2(k))+1));
        //cout << den << endl;
        first = second = (n-k)/den;
        if (n>=k*2 && (n-k)%den != 0) first++;*/

        printf("Case #%d: %llu %llu\n", ++caseno, first, second);
    }
    return 0;
}

