provider "aws" {
  region = "ap-south-1"
}

provider "aws" {
  alias  = "another-region"
  region = "us-west-2"
}
