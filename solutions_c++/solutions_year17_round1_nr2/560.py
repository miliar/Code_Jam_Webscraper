#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int N, P;
    cin >> N >> P;
    vector<int> R(N);
    for (int i=0; i<N; i++) cin >> R[i];
    vector< vector<int> > Q(N, vector<int>(P,0) );
    for (int i=0; i<N; i++) 
      for (int j=0; j<P; j++)
	cin >> Q[i][j];
    // Make Q row monitone
    for (int i=0; i<N; i++) 
      sort(Q[i].begin(),Q[i].end());

    vector< vector<int> > Lo(N, vector<int>(P,0) );
    vector< vector<int> > Hi(N, vector<int>(P,0) );

    for (int i=0; i<N; i++) 
      for (int j=0; j<P; j++) {
	Hi[i][j] = 10*Q[i][j] / (R[i] *9);
	Lo[i][j] = (10*Q[i][j] + (11 * R[i]-1))/ (11 * R[i]);
      }
    
    long long answer = 0;

    vector<int> idx(N,0);

    bool done = false;

    while (! done) {
      int s = 0;
      for (int i=0; i<N; i++) {
	while (! done && idx[i]<P && Lo[i][idx[i]]>Hi[i][idx[i]])
	  idx[i]++;
	if (idx[i] >= P) done = true;
	if (! done) s = max(s,Lo[i][idx[i]]);
      }
      if (! done) {
	bool valid = true;
	for (int i=0; i<N; i++)
	  if (! (Lo[i][idx[i]]<=s && s <=Hi[i][idx[i]]) )
	      valid = false;

	if (valid) {
	  answer++;
	  for (int i=0; i<N; i++) idx[i] ++;
	} else {
	  for (int i=0; i<N; i++)
	    if (Hi[i][idx[i]]<s)
	      idx[i] ++;
	};

      };
    };
    
    cout << "Case #" << t << ": " << answer << endl;

    /*
    for (int i=0; i<N; i++) {
      for (int j=0; j<P; j++)
	cout << Q[i][j] << ":" << Lo[i][j] << "-" << Hi[i][j] << " ";
      cout << endl;
    }
    */
    
  }
};
