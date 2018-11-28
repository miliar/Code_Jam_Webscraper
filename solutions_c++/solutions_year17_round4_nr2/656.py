#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <unistd.h>
#include <unordered_set>
#include <sstream>
#include <set>
#include <map>

using namespace std;

string problem = "/Users/alanpierce/codejam17/Round2/B-large";
FILE *infile;
FILE *outfile;

typedef long long lld;

lld next_lld() {
    lld result = 0;
    fscanf(infile, "%lld", &result);
    return result;
}

string next_string() {
    char result[100000];
    fscanf(infile, "%s", result);
    return string(result);
}

int next_int() {
    int result = 0;
    fscanf(infile, "%d", &result);
    return result;
}

vector<int> next_int_vector(int n) {
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        result[i] = next_int();
    }
    return result;
}

string handle_case() {
    int num_seats = next_int();
    int num_customers = next_int();
    int num_tickets = next_int();
    vector<pair<int, int>> tickets;
    for (int i = 0; i < num_tickets; i++) {
        tickets.push_back(make_pair(next_int() - 1, next_int() - 1));
    }

    int max_tickets_per_person = 0;
    map<int, int> num_tickets_by_person;
    for (int i = 0; i < tickets.size(); i++) {
        num_tickets_by_person[tickets[i].second]++;
        if (num_tickets_by_person[tickets[i].second] > max_tickets_per_person) {
            max_tickets_per_person = num_tickets_by_person[tickets[i].second];
        }
    }

    vector<int> num_tickets_by_position(num_seats);
    for (int i = 0; i < tickets.size(); i++) {
        num_tickets_by_position[tickets[i].first]++;
    }

    int width = max_tickets_per_person;
    int num_available = 0;

    for (int position = 0; position < num_tickets_by_position.size(); position++) {
        int seat_tickets = num_tickets_by_position[position];
        num_available += width;

        while (seat_tickets > num_available) {
            width++;
            num_available += position + 1;
        }
        num_available -= seat_tickets;
    }

    int num_promotions = 0;
    num_available = 0;
    for (int position = 0; position < num_tickets_by_position.size(); position++) {
        int seat_tickets = num_tickets_by_position[position];

        int num_immediately_available = width;
        if (seat_tickets <= num_immediately_available) {
            num_available += num_immediately_available - seat_tickets;
        } else {
            seat_tickets -= num_immediately_available;
            num_promotions += seat_tickets;
            num_available -= seat_tickets;
            if (num_available < 0) {
                printf("Crap!!!\n");
            }
        }
    }

    stringstream ss;
    ss << width << " " << num_promotions;
    return ss.str();
}

int main() {
    string infilename = problem + ".in";
    string outfilename = problem + ".out";
    infile = fopen(infilename.c_str(), "r");
    if (infile == nullptr) {
        printf("File %s not found!", infilename.c_str());
        return 1;
    }
    outfile = fopen(outfilename.c_str(), "w");

    lld n_cases = next_lld();
    for (lld case_num = 1; case_num <= n_cases; ++case_num) {
        string result = handle_case();
        printf("Case #%lld: %s\n", case_num, result.c_str());
        fprintf(outfile, "Case #%lld: %s\n", case_num, result.c_str());
    }
    return 0;
}