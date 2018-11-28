#include <cstdio>
#include <iostream>
#include <list>
#include <set>
#include <unordered_set>


using namespace std;

#define PI 3.14159265358979323846264338327950288419716939937510582l

class Pancake {
public:
	int mRadius;
	int mWidth;
	long double borderArea;
	long double surfaceArea;

	Pancake (int radius, int width);

private:
	long double BorderArea () const;
	long double SurfaceArea () const;
};

Pancake::Pancake (int radius, int width) {
	mRadius = radius;
	mWidth = width;
	borderArea = BorderArea ();
	surfaceArea = SurfaceArea ();
}

long double Pancake::BorderArea () const {
	return 2.0l * PI * static_cast<long double> (mRadius) * static_cast<long double> (mWidth);
}

long double Pancake::SurfaceArea () const {
	return  PI * static_cast<long double> (mRadius) * static_cast<long double> (mRadius);
}

vector<Pancake> pancakes;

struct BorderComparer {
	bool operator() (const int& lhs, const int& rhs) const {
		return pancakes[lhs].borderArea == pancakes[rhs].borderArea && pancakes[lhs].mRadius == pancakes[rhs].mRadius ? lhs < rhs : pancakes[lhs].borderArea == pancakes[rhs].borderArea ? pancakes[lhs].mRadius < pancakes[rhs].mRadius : pancakes[lhs].borderArea < pancakes[rhs].borderArea;
	}
};

struct RadiusComparer {
	bool operator() (const int& lhs, const int& rhs) const {
			return pancakes[lhs].mRadius == pancakes[rhs].mRadius && pancakes[lhs].mWidth == pancakes[rhs].mWidth ? lhs < rhs : pancakes[lhs].mRadius == pancakes[rhs].mRadius ? pancakes[lhs].mWidth > pancakes[rhs].mWidth : pancakes[lhs].mRadius > pancakes[rhs].mRadius;
	}
};

int main () {
	ios_base::sync_with_stdio (false), cin.tie (nullptr);

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int tc = 0; tc < t; tc++) {
		int n, k;
		scanf ("%d %d", &n, &k);
	
		pancakes.clear ();
		for(int i = 0; i < n; i++) {
			int r, h;
			scanf ("%d %d", &r, &h);
			pancakes.emplace_back (r, h);
		}

		long double result = 0.0l;
		set<int, BorderComparer> thicknessOrder;
		set<int, RadiusComparer> radiusOrder;
		for(int i = 0; i < n; i++) {
			result += pancakes[i].borderArea;
			thicknessOrder.insert (i);
			radiusOrder.insert (i);
		}
		result += pancakes[*radiusOrder.begin ()].surfaceArea;
		thicknessOrder.erase (*radiusOrder.begin ());

		for(int i = n; i > k; i--) {
			auto pIt = radiusOrder.begin ();
			long double bottom = pancakes[*pIt].borderArea + pancakes[*pIt].surfaceArea - pancakes[*(++pIt)].surfaceArea;
			if(bottom < pancakes[*thicknessOrder.begin()].borderArea) {
				result -= bottom;
				radiusOrder.erase (radiusOrder.begin ());
				thicknessOrder.erase (*radiusOrder.begin ());
			} else {
				result -= pancakes[*thicknessOrder.begin ()].borderArea;
				radiusOrder.erase (*thicknessOrder.begin ());
				thicknessOrder.erase (thicknessOrder.begin ());
			}
		}
		
		printf ("Case #%d: %.9lf\n", tc + 1, result);
	}


	fflush (stdout);
	fclose (stdin);
	fclose (stdout);

	return 0;
}
