#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

class pancake {
public:
	int r, h, _id;
	double heightScore, radiusScore;

	pancake(int r, int h) : r(r), h(h) {
		static int id = 0;
		heightScore = 2 * M_PI * r * h;
		radiusScore = M_PI * r * r;
		_id = id++;
	}

	bool operator==(pancake& rhs) const{
		return rhs._id == _id;
	}
};

bool compareByR(const pancake & a, const pancake & b)
{
    return a.r > b.r;
}

bool compareByHeightScore(const pancake & a, const pancake & b)
{
    return a.heightScore > b.heightScore;
}

int main() {
  std::cout << std::fixed;
  std::cout << std::setprecision(9);

  int t;
  cin >> t; 
  for (int i = 1; i <= t; ++i) {
    int n, k;
    cin >> n >> k;

   	vector<pancake> pancakes;
    for(int j = 0; j < n; j++) {
    	int r, h;
    	cin >> r >> h;
    	pancakes.push_back(pancake(r, h));
    }

    vector<pancake> sortedByR, sortedByHeightScore;

    std::sort(pancakes.begin(), pancakes.end(), compareByR);
    sortedByR = pancakes;

    std::sort(pancakes.begin(), pancakes.end(), compareByHeightScore);
    sortedByHeightScore = pancakes;

    double maxScore = 0;
    for(int j = 0; j < n - k + 1; j++) {
    	int startR = sortedByR[j].r;
    	double score = sortedByR[j].radiusScore + sortedByR[j].heightScore;
    	//cout << "Starting with radius: " << startR << endl;

    	int taken = 1;
    	for(int m = 0; m < sortedByHeightScore.size() && taken < k; m++) {
    		if(sortedByHeightScore[m].r <= startR && !(sortedByHeightScore[m] == sortedByR[j])) {
    			//cout << "Adding pancake with radius: " << sortedByHeightScore[m].r << endl;
    			score += sortedByHeightScore[m].heightScore;
    			taken += 1;
    		}
    	}

    	maxScore = max(maxScore, score);
    }


    cout << "Case #" << i << ": " << maxScore << endl;
  }

  return 0;
}