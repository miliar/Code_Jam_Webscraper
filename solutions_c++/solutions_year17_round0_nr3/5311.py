#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<sys/mman.h>
#include<set>

using namespace std;

#define VNAME(x) #x

const int PAGE_SHIFT = 12;
const int INPUT_MAXSIZE = 1;
const char ZERO = '0';
const char ONE = '1';
const char* LINE = "%lld %lld\n";
const char* HEADER = "Case #%d: ";

typedef struct {
  long long value;
  long long limit;
} testCase;

typedef struct {
  long long max;
  long long min;
} testOutput;

static inline int pagesize() {
  return INPUT_MAXSIZE*(1 << PAGE_SHIFT);
}

static inline int getmemflags() {
  return MAP_ANONYMOUS|MAP_PRIVATE|MAP_NORESERVE|MAP_LOCKED;
}

static inline int parseInteger() {
  static int res = 0;
  scanf("%d", &res);
  return res;
}

static inline void showOutput(testOutput* result) {
  printf("%lld %lld", result->max, result->min);
}

static inline void parseNewline() {
  scanf("\n");
}

static inline void showNewline() {
  printf("\n");
}

static inline char* allocateBuffer() { 
  void* result = mmap(NULL, pagesize(), PROT_READ|PROT_WRITE, getmemflags(), -1, 0);
  if(result == MAP_FAILED) {
    printf(VNAME(MAP_FAILED));
    showNewline();
    _exit(EXIT_FAILURE);
  }
  return (char*)result;
}

static inline const testCase* parseLine() {
  static testCase inputBuffer = {
    .value = 0,
    .limit = 0
  };
  scanf(LINE, &inputBuffer.value, &inputBuffer.limit);
  return &inputBuffer;
}

static inline void showHeader(int testCaseId) {
  printf(HEADER, testCaseId); 
}

static inline char getBit(long long value) {
  char result = 0;
  switch(value){
  case 0:
    result = ZERO;
    break;
  case 1:
    result = ONE;
    break;
  default:
    break;
  }
  return result;
}

static inline long long getValue(char bit) {
  long long result = 0;
  if(bit == ONE) {
    result = 1;
  }
  return result;
}

static inline void load(char* bitSet, long long value) {
  int position = 0;
  while(value > 0) {
    bitSet[position] = getBit(value%2);
    value /= 2;
    ++position;
  }
  bitSet[position] = value;
}

static inline void process(const testCase* input, testOutput* output) {
  static multiset<long long> values; 
  long long res = 0;
  values.clear();
  values.insert(-input->value);
  for(int i=0; i<input->limit; ++i) {
    res = -(*values.begin());
    values.erase(values.begin());
    output->max = res/2;
    if(res%2 == 0) {      
      output->min = res/2-1;
    }
    else {
      output->min = res/2;
    }
    values.insert(-output->max);
    values.insert(-output->min);
  }
}

static inline void execute() {  
  static testOutput outputBuffer = {
    .max = 0,
    .min = 0
  };
  const testCase* inputBuffer = parseLine();
  process(inputBuffer, &outputBuffer);
  showOutput(&outputBuffer);
}

static inline int run(int tests) {
  parseNewline();
  for(int i=1; i<=tests; ++i) {
    showHeader(i);
    execute();
    showNewline();
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);
}
